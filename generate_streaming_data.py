import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta
from sqlalchemy import create_engine

# Database Connection
engine = create_engine('postgresql://postgres:umeanor01@localhost:5432/streaming_qoe_db')

print("Generating streaming library dimensions...")

# 1. Populate dim_content
genres = ['Action', 'Comedy', 'Drama', 'Sci-Fi', 'Documentary', 'Thriller']
content_library = []
for i in range(100):
    content_library.append({
        "content_id": f"VID-{10000+i}",
        "title": f"The {random.choice(genres)} Masterpiece Volume {i}",
        "genre": random.choice(genres)
    })
pd.DataFrame(content_library).to_sql('dim_content', engine, if_exists='append', index=False)

# 2. Populate dim_subscribers
plans = ['Basic', 'Standard', 'Premium']
subscribers = []
base_date = datetime(2026, 1, 1)

for i in range(2000):
    subscribers.append({
        "subscriber_id": f"SUB-{8000+i}",
        "signup_date": (base_date - timedelta(days=random.randint(0, 90))).date(),
        "subscription_plan": random.choice(plans)
    })
pd.DataFrame(subscribers).to_sql('dim_subscribers', engine, if_exists='append', index=False)

print("Simulating streaming sessions with embedded QoE issues...")

# Fetch surrogate keys for structural mapping
sub_keys = pd.read_sql("SELECT subscriber_key FROM dim_subscribers", engine)['subscriber_key'].tolist()
con_keys = pd.read_sql("SELECT content_key FROM dim_content", engine)['content_key'].tolist()

devices = ['Smart TV', 'Mobile App', 'Web Browser', 'Gaming Console']
sessions = []
analysis_start = datetime(2026, 3, 1)

for i in range(20000):
    sub_key = random.choice(sub_keys)
    con_key = random.choice(con_keys)
    s_date = analysis_start + timedelta(days=random.randint(0, 60))
    
    # Baseline metrics
    minutes_watched = round(random.uniform(5.0, 150.0), 2)
    buffering_sec = random.choices([0, random.randint(1, 10), random.randint(30, 300)], weights=[75, 20, 5])[0]
    
    # Injecting Churn Drivers: If buffering is severe, drop minutes watched significantly
    if buffering_sec > 30:
        minutes_watched = round(random.uniform(1.0, 12.0), 2)
        
    # Injecting Content Fatigue: Force specific subscriber ranges to watch almost nothing in late April
    if sub_key in sub_keys[:150] and s_date > datetime(2026, 4, 15):
        minutes_watched = round(random.uniform(0.5, 4.0), 2)
        buffering_sec = 0 # Technical side is perfect, they are just bored!

    sessions.append({
        "subscriber_key": sub_key,
        "content_key": con_key,
        "session_date": s_date.date(),
        "minutes_watched": minutes_watched,
        "buffering_duration_sec": buffering_sec,
        "device_type": random.choice(devices)
    })

pd.DataFrame(sessions).to_sql('fact_stream_sessions', engine, if_exists='append', index=False)
print(f"Successfully generated and injected {len(sessions)} streaming system logs into PostgreSQL.")
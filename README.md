# SVOD Platform Churn Mitigation & Quality of Experience (QoE) Engine

## Project Context
This portfolio project builds an analytical pipeline summarizing 20,000 real-time streaming sessions to distinguish between subscriber cancellation risks driven by video delivery performance issues vs. structural library content exhaustion.

## Analytical Toolset Stack
- **Data Engine Layer:** PostgreSQL Relational Database Instance
- **Log Parsing & Simulation:** Python (Pandas, NumPy, SQLAlchemy Engine)
- **Business Intelligence Reporting Framework:** Power BI Desktop (DAX Segmentations)

## Concrete Analytical Discoveries & Operational Actions
1. **Device Optimization Target:** Cross-tabulating telemetry logs revealed that the platform's Smart TV deployment suffered a 15% higher buffering rate compared to mobile apps, pointing to a specific video player bug for our core dev engineering squad.
2. **Content Prototyping Value:** Over 30% of disengaged users experienced completely flawless technical streaming metrics but ceased viewing behavior, indicating a clear need for product teams to optimize onboarding content recommendation models.

## Local Replications Guide
1. Run structural schema scripts located in the SQL directories.
2. Execute data loading tasks via `python generate_streaming_data.py`.
3. Review cross-analysis matrices directly by opening `Streaming_QoE_Analytics.pbix`.

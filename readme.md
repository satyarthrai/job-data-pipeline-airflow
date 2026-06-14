📊Data & AI Field Job Finder & Analytics Pipeline

(Python + Airflow + MySQL + PowerBI + Docker)

--->  Overview

This project is an end-to-end data engineering + analytics system that collects job postings from multiple APIs, filters only DATA & AI RELATED JOBS , stores them in a database, and prepares the data for dashboard visualization and insights.

It demonstrates a complete workflow:

Data Extraction → Transformation → Storage → Analytics → Dashboarding->Automation

---> Problem Statement

Job platforms contain thousands of listings, but users interested in Data Science, Data Analytics, and Data Engineering roles struggle to filter relevant opportunities.

This system solves that by:

Aggregating job data from multiple sources
Filtering only Data-related jobs
Structuring and storing clean datasets
Preparing data for analytics dashboards
Automating everything using Airflow

:: System Architecture
           ┌────────────────────┐
           │   RemoteOK API     │
           └────────────────────┘
                     │
           ┌────────────────────┐
           │   Arbeitnow API    │
           └────────────────────┘
                     │
           ┌────────────────────┐
           │  Himalayas API     │
           └────────────────────┘
                     │
                     ▼
        ┌──────────────────────────┐
        │   AIRFLOW ORCHESTRATION  │
        │                          │
        │  1. Extract Jobs         │
        │  2. Filter Data Roles    │
        │  3. Transform Dataset    │
        │  4. Load to MySQL        │
        │  5. Save JSON Backup     │
        └──────────────────────────┘
                     │
                     ▼
        ┌──────────────────────────┐
        │      MYSQL DATABASE      │
        └──────────────────────────┘
                     │
                     ▼
        ┌──────────────────────────┐
        │   ANALYTICS DASHBOARD    │
        │ (Power BI / Tableau)     │
        └──────────────────────────┘

--->Tech Stack

Apache Airflow → Workflow orchestration
Docker → Containerized environment
MySQL → Structured data storage
Python → ETL logic
Requests → API calls
Power BI / Tableau → Dashboard & insights
JSON → Backup layer

📂 Project Structure

project-root/
│
├── data/
│   ├── raw/                    # Raw API data
│   └── processed/              # Cleaned & filtered datasets
│
├── dags/                       # Airflow DAGs
│   └── job_data_pipeline.py
│
├── src/                        
│
├── sql/                       # SQL scripts
│   ├── schema.sql
│   └── queries.sql
│
├── logs/                      # Airflow logs
│
├── main.py                    
│
├── powerbi_dashboard_img/     # Dashboard screenshots
│
├── docker-compose.yml
└── README.md

# Pipeline Workflow
1. Extract (Data Collection)

Data is pulled from multiple job APIs:

RemoteOK
Arbeitnow
Himalayas

2. Transform (Filtering Logic)

Only relevant Data domain jobs are kept:

data analyst
data engineer
data scientist
machine learning engineer
business intelligence
analytics roles

Irrelevant jobs are removed.

3. Load (Storage Layer)

Cleaned data is stored in:

MySQL database (structured tables)
Backup JSON file (raw snapshot)

4. Analytics Layer

Stored data is used to build dashboards such as:

📊 Total Data Jobs Available
🏢 Top Hiring Companies
📍 Location distribution
📈 Trend of job postings
📊 Dashboard Preview 

build dashboards using:
Power BI

❗ Challenges Faced

Docker port conflicts (MySQL 3306 issue)
Airflow authentication setup confusion
Multi-container networking (service naming)
Handling inconsistent API responses
DAG task failures due to data schema mismatch

🧠 Key Learnings

End-to-end ETL pipeline design
Airflow DAG orchestration
Docker-based infrastructure setup
API data ingestion at scale
Data filtering & transformation logic
Preparing data for analytics dashboards

🚀 Future Improvements
Add PostgreSQL / Data Warehouse layer
Add dbt transformations
Deploy on cloud (AWS / GCP)
Add real-time streaming (Kafka)
Automate dashboard refresh
Add job recommendation system

👨‍💻 Author
Satyarth Rai
B.Tech Student | Data Analytics & Engineering Enthusiast


If you like this project
Give a ⭐ on GitHub and explore improvements!
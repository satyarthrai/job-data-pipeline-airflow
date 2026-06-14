📊 Data & AI Field Job Finder & Analytics Pipeline

#Project Overview

This project is an end-to-end data engineering and analytics pipeline that collects job postings from multiple APIs, filters only Data & AI related roles, stores structured data in a database, and prepares it for dashboard-based insights.

The system demonstrates a complete data workflow:

Data Extraction → Transformation → Storage → Analytics → Dashboarding → Automation (Airflow)

#Business Problem

Job boards contain thousands of listings across multiple domains, making it difficult for students and professionals to find relevant Data Science, Data Analytics, Data Engineering, and AI roles.

This pipeline solves the problem by:

Aggregating job data from multiple APIs
Filtering only Data & AI related roles
Structuring and cleaning job data
Storing data for analysis
Automating the process using Apache Airflow

#Tools Used

🐍 Python
API Integration (Requests)
Data Cleaning & Filtering
ETL Logic Implementation

🌬 Apache Airflow
Workflow Orchestration
DAG Scheduling
Task Automation

🐬 MySQL
Structured Data Storage
Query-Based Analysis

🐳 Docker
Containerized Airflow Environment

📊 Power BI
Dashboard Creation
Business Insights & Visualization

Data Sources Used

RemoteOK API
Remote job listings

Arbeitnow API
Global job postings

Himalayas API
Tech-focused job listings

Each API provides unstructured job data which is standardized in the pipeline.

#Data Engineering Process
1. Data Extraction

Data is pulled from multiple APIs:

RemoteOK
Arbeitnow
Himalayas
2. Data Transformation

Only relevant Data & AI jobs are filtered using keywords:

data analyst
data engineer
data scientist
machine learning engineer
business intelligence
analytics roles

Irrelevant job postings are removed.

3. Data Storage

Processed data is stored in:

MySQL database (structured storage)
JSON backup file (raw snapshot layer)
4. Workflow Automation (Airflow)

The entire pipeline is automated using an Airflow DAG:

Extract data from APIs
Transform & filter jobs
Load into database
Save backup dataset
Database Design
Table: job_data

Key Fields:

job_title
company
location
job_type
source
apply_link
description


Airflow DAG Structure

DAG: job_data_pipeline
Tasks:
run_pipeline → Executes full ETL pipeline

Workflow:

Extract → Transform → Load → Backup

Power BI Dashboard

: Job Market Overview
Total Data & AI Jobs Available
Source-wise Job Distribution
Job Type Breakdown

: Demand Analysis
Top Hiring Companies
Location-wise Job Distribution
Remote vs Onsite Trends

#Project Structure

project-root/

├── data/
│   ├── raw/                 # Raw API data
│   └── processed/           # Cleaned dataset
│
├── dags/
│   └── job_data_pipeline.py
│
├── src/                     # ETL Logic
│
├── sql/
│
├── logs/                    # Airflow logs
│
├── main.py                  # Local pipeline runner (optional)
│
├── powerbi_dashboard_img/   # Dashboard screenshots
│
├── docker-compose.yml
└── README.md

Future Improvements

Add PostgreSQL / Data Warehouse layer
Modularize ETL using src/ structure
Add dbt transformations
Deploy pipeline on cloud (AWS / GCP)
Add real-time ingestion (Kafka)
Build job recommendation engine

Key Outcome

This project delivers a fully automated data pipeline that collects and processes real-time job postings and transforms them into structured, analytics-ready datasets for career insights in the Data & AI domain.

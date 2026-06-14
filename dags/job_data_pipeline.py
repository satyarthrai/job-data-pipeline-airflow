from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import requests
import json
import os
import mysql.connector

# -----------------------
# PATH (backup file)
# -----------------------
OUTPUT_PATH = "/opt/airflow/data/raw/airflow_jobs.json"

# -----------------------
# EXTRACT FUNCTIONS
# -----------------------

def fetch_remoteok():
    url = "https://remoteok.com/api"
    res = requests.get(url)
    return res.json()[1:]

def fetch_arbeitnow():
    url = "https://www.arbeitnow.com/api/job-board-api"
    res = requests.get(url)
    return res.json()["data"]

def fetch_himalayas():
    url = "https://himalayas.app/jobs/api"
    res = requests.get(url)
    return res.json()["jobs"]

# -----------------------
# TRANSFORM
# -----------------------

def filter_jobs(ti):
    remoteok = ti.xcom_pull(task_ids="extract_remoteok")
    arbeitnow = ti.xcom_pull(task_ids="extract_arbeitnow")
    himalayas = ti.xcom_pull(task_ids="extract_himalayas")

    all_jobs = remoteok + arbeitnow + himalayas

    keywords = ["data", "analyst", "data engineer", "data scientist", "bi", "machine learning"]

    filtered = []
    for job in all_jobs:
        title = str(job.get("position") or job.get("title") or "").lower()

        if any(k in title for k in keywords):
            filtered.append(job)

    ti.xcom_push(key="filtered_jobs", value=filtered)
    return filtered

# -----------------------
# LOAD (MySQL)
# -----------------------

def load_to_mysql(ti):
    jobs = ti.xcom_pull(task_ids="filter_jobs", key="filtered_jobs")

    conn = mysql.connector.connect(
        host="mysql",
        user="root",
        password="root",
        database="airflow_db"
    )

    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS jobs (
            id INT AUTO_INCREMENT PRIMARY KEY,
            title TEXT,
            company TEXT,
            location TEXT
        )
    """)

    for job in jobs:
        title = job.get("position") or job.get("title")
        company = job.get("company") or "Unknown"
        location = job.get("location") or "Remote"

        cursor.execute(
            "INSERT INTO jobs (title, company, location) VALUES (%s, %s, %s)",
            (title, company, location)
        )

    conn.commit()
    cursor.close()
    conn.close()

# -----------------------
# BACKUP JSON
# -----------------------

def save_json(ti):
    jobs = ti.xcom_pull(task_ids="filter_jobs", key="filtered_jobs")

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)

    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        json.dump(jobs, f, indent=2)

# -----------------------
# DAG
# -----------------------

default_args = {
    "start_date": datetime(2024, 1, 1),
}

with DAG(
    dag_id="job_data_pipeline",
    default_args=default_args,
    schedule_interval=None,
    catchup=False
) as dag:

    # EXTRACT TASKS
    extract_remoteok = PythonOperator(
        task_id="extract_remoteok",
        python_callable=fetch_remoteok
    )

    extract_arbeitnow = PythonOperator(
        task_id="extract_arbeitnow",
        python_callable=fetch_arbeitnow
    )

    extract_himalayas = PythonOperator(
        task_id="extract_himalayas",
        python_callable=fetch_himalayas
    )

    # TRANSFORM
    transform = PythonOperator(
        task_id="filter_jobs",
        python_callable=filter_jobs
    )

    # LOAD
    load = PythonOperator(
        task_id="load_to_mysql",
        python_callable=load_to_mysql
    )

    # BACKUP
    backup = PythonOperator(
        task_id="save_json",
        python_callable=save_json
    )

    # -----------------------
    # DEPENDENCIES
    # -----------------------

    [extract_remoteok, extract_arbeitnow, extract_himalayas] >> transform >> load >> backup
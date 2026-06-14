import pandas as pd
import mysql.connector
import numpy as np

# =========================
# Read CSV
# =========================

df = pd.read_csv("data/processed/data_jobs.csv")

# Convert NaN to None
df = df.replace({np.nan: None})

print(f"Rows Found: {len(df)}")

# =========================
# Connect MySQL
# =========================

conn = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="IamyashraI8765",
    database="job_market_db"
)

cursor = conn.cursor()

# =========================
# Insert Query
# =========================

insert_query = """
INSERT INTO jobs (
    job_id,
    source,
    job_title,
    job_category,
    company_name,
    location,
    date_posted,
    salary_min,
    salary_max,
    skills,
    description,
    job_url,
    load_date
)
VALUES (
    %s,%s,%s,%s,%s,%s,%s,
    %s,%s,%s,%s,%s,%s
)
"""

# =========================
# Load Data
# =========================

success_count = 0

for index, row in df.iterrows():

    values = (
        row["job_id"],
        row["source"],
        row["job_title"],
        row["job_category"],
        row["company_name"],
        row["location"],
        row["date_posted"],
        row["salary_min"],
        row["salary_max"],
        row["skills"],
        row["description"],
        row["job_url"],
        row["load_date"]
    )

    try:
        cursor.execute(insert_query, values)
        success_count += 1

    except Exception as e:

        print("\n" + "="*60)
        print(f"ERROR AT ROW: {index}")
        print("="*60)

        print("\nVALUES:")
        print(values)

        print("\nERROR:")
        print(e)

        break

# =========================
# Commit
# =========================

conn.commit()

print("\n" + "="*60)
print(f"Successfully Loaded: {success_count} Rows")
print("="*60)

cursor.close()
conn.close()
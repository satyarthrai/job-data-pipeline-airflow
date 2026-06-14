import json
import pandas as pd
from pathlib import Path
from datetime import datetime


POSITIVE_KEYWORDS = [

    # Data

    "data analyst",
    "data engineer",
    "data scientist",
    "analytics engineer",
    "data architect",
    "data modeler",
    "data platform",

    # BI

    "business intelligence",
    "bi analyst",
    "bi developer",
    "power bi",
    "tableau",

    # ML / AI

    "machine learning",
    "ml engineer",
    "mlops",
    "ai engineer",
    "ai researcher",
    "applied ai",
    "research scientist",

    # Analytics

    "analytics manager",
    "analytics specialist",
    "predictive analytics",
    "marketing analytics",

    # Related

    "decision scientist",
    "insights analyst",
    "reporting analyst"
]

NEGATIVE_KEYWORDS = [

    "assistant",
    "customer",
    "billing",
    "carrier",
    "counsel",
    "sales",
    "recruiter",
    "talent",
    "operations manager",
    "legal",
    "claims",
    "advisor",
    "support analyst",
    "hris analyst"
]


def is_data_role(title):

    if not title:
        return False

    title = str(title).lower()

    positive_match = any(
        keyword in title
        for keyword in POSITIVE_KEYWORDS
    )

    negative_match = any(   
        keyword in title
        for keyword in NEGATIVE_KEYWORDS
    )

    return positive_match and not negative_match
def get_job_category(title):

    if not title:
        return "Other"

    title = str(title).lower()

    # Data Engineer

    if any(keyword in title for keyword in [
        "data engineer",
        "data platform",
        "data architect",
        "data modeler"
    ]):
        return "Data Engineer"

    # Data Analyst

    if any(keyword in title for keyword in [
        "data analyst",
        "business analyst",
        "research data analyst"
    ]):
        return "Data Analyst"

    # Business Intelligence

    if any(keyword in title for keyword in [
        "business intelligence",
        "bi analyst",
        "power bi",
        "tableau"
    ]):
        return "BI / Analytics"

    # Data Scientist

    if any(keyword in title for keyword in [
        "data scientist",
        "research scientist",
        "decision scientist"
    ]):
        return "Data Scientist"

    # Machine Learning

    if any(keyword in title for keyword in [
        "machine learning",
        "ml engineer",
        "mlops"
    ]):
        return "Machine Learning"

    # AI

    if any(keyword in title for keyword in [
        "ai engineer",
        "applied ai",
        "generative ai",
        "ai/ml"
    ]):
        return "Artificial Intelligence"

    return "Other"

def transform_remoteok():

    records = []

    with open(
        "data/raw/remoteok_jobs.json",
        "r",
        encoding="utf-8"
    ) as f:

        jobs = json.load(f)

    for job in jobs:

        if not isinstance(job, dict):
            continue

        title = job.get("position")

        if not is_data_role(title):
            continue

        records.append({
            "job_id": job.get("id"),
            "source": "RemoteOK",
            "job_title": title,
            "job_category": get_job_category(title),
            "company_name": job.get("company"),
            "location": job.get("location"),
            "date_posted": job.get("date"),
            "salary_min": job.get("salary_min"),
            "salary_max": job.get("salary_max"),
            "skills": ", ".join(job.get("tags", [])),
            "description": job.get("description"),
            "job_url": job.get("url")
        })

    return records


def transform_arbeitnow():

    records = []

    with open(
        "data/raw/arbeitnow_jobs.json",
        "r",
        encoding="utf-8"
    ) as f:

        data = json.load(f)

    for job in data["data"]:

        title = job.get("title")

        if not is_data_role(title):
            continue

        records.append({
            "job_id": job.get("slug"),
            "source": "Arbeitnow",
            "job_title": title,
            "job_category": get_job_category(title),
            "company_name": job.get("company_name"),
            "location": job.get("location"),
            "date_posted": job.get("created_at"),
            "salary_min": None,
            "salary_max": None,
            "skills": ", ".join(job.get("tags", [])),
            "description": job.get("description"),
            "job_url": job.get("url")
        })

    return records


def transform_himalayas():

    records = []

    with open(
        "data/raw/himalayas_jobs.json",
        "r",
        encoding="utf-8"
    ) as f:

        data = json.load(f)

    for job in data["jobs"]:

        title = job.get("title")

        if not is_data_role(title):
            continue

        records.append({
            "job_id": job.get("guid"),
            "source": "Himalayas",
            "job_title": title,
            "job_category": get_job_category(title),
            "company_name": job.get("companyName"),
            "location": ", ".join(
                job.get("locationRestrictions", [])
            ),
            "date_posted": job.get("pubDate"),
            "salary_min": job.get("minSalary"),
            "salary_max": job.get("maxSalary"),
            "skills": ", ".join(
                job.get("categories", [])
            ),
            "description": job.get("description"),
            "job_url": job.get("applicationLink")
        })

    return records


def run_transformation():

    all_jobs = []

    all_jobs.extend(transform_remoteok())
    all_jobs.extend(transform_arbeitnow())
    all_jobs.extend(transform_himalayas())

    df = pd.DataFrame(all_jobs)

    df["load_date"] = datetime.today().date()

    processed_path = Path("data/processed")
    processed_path.mkdir(
        parents=True,
        exist_ok=True
    )

    output_file = (
        processed_path / "data_jobs.csv"
    )

    df.to_csv(
        output_file,
        index=False
    )

    print("=" * 50)
    print("TRANSFORMATION COMPLETE")
    print("=" * 50)

    print(
        f"Data Jobs Found: {len(df)}"
    )

    print(
        f"Output File: {output_file}"
    )

    return df


if __name__ == "__main__":

    run_transformation()

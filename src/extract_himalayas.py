import requests
import json
from pathlib import Path


def extract_himalayas(max_pages=50):

    print("Fetching Himalayas...")

    all_jobs = []

    limit = 20
    offset = 0

    for page in range(max_pages):

        url = (
            f"https://himalayas.app/jobs/api"
            f"?limit={limit}&offset={offset}"
        )

        response = requests.get(
            url,
            headers={"User-Agent": "Mozilla/5.0"},
            timeout=30
        )

        response.raise_for_status()

        data = response.json()

        jobs = data.get("jobs", [])

        if not jobs:
            break

        all_jobs.extend(jobs)

        print(
            f"Page {page+1}: "
            f"{len(jobs)} jobs "
            f"(Total: {len(all_jobs)})"
        )

        offset += limit

    raw_path = Path("data/raw")
    raw_path.mkdir(parents=True, exist_ok=True)

    filepath = raw_path / "himalayas_jobs.json"

    with open(filepath, "w", encoding="utf-8") as f:

        json.dump(
            {
                "total_records": len(all_jobs),
                "jobs": all_jobs
            },
            f,
            indent=4
        )

    print(
        f"\nHimalayas Records Saved: {len(all_jobs)}"
    )

    return len(all_jobs)
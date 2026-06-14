import requests
import json
from pathlib import Path


def extract_remoteok():

    print("Fetching RemoteOK...")

    url = "https://remoteok.com/api"

    response = requests.get(
        url,
        headers={"User-Agent": "Mozilla/5.0"},
        timeout=30
    )

    response.raise_for_status()

    jobs = response.json()

    raw_path = Path("data/raw")
    raw_path.mkdir(parents=True, exist_ok=True)

    filepath = raw_path / "remoteok_jobs.json"

    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(jobs, f, indent=4)

    print(f"RemoteOK Records: {len(jobs)}")

    return len(jobs)
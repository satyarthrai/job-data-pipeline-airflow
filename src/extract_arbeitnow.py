import requests
import json
from pathlib import Path


def extract_arbeitnow():

    print("Fetching Arbeitnow...")

    url = "https://www.arbeitnow.com/api/job-board-api"

    response = requests.get(
        url,
        headers={"User-Agent": "Mozilla/5.0"},
        timeout=30
    )

    response.raise_for_status()

    data = response.json()

    raw_path = Path("data/raw")
    raw_path.mkdir(parents=True, exist_ok=True)

    filepath = raw_path / "arbeitnow_jobs.json"

    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

    print(f"Arbeitnow Records: {len(data['data'])}")

    return len(data["data"])
from src.extract_remoteok import extract_remoteok
from src.extract_arbeitnow import extract_arbeitnow
from src.extract_himalayas import extract_himalayas

from datetime import datetime


def main():

    print("=" * 60)
    print("JOB MARKET INTELLIGENCE PLATFORM")
    print("=" * 60)

    start_time = datetime.now()

    try:

        remoteok_count = extract_remoteok()

        arbeitnow_count = extract_arbeitnow()

        himalayas_count = extract_himalayas()

        print("\n" + "=" * 60)
        print("RAW DATA INGESTION SUCCESSFUL")
        print("=" * 60)

        print(f"RemoteOK Records  : {remoteok_count}")
        print(f"Arbeitnow Records : {arbeitnow_count}")
        print(f"Himalayas Records : {himalayas_count}")

        print(
            f"\nExecution Time: {datetime.now() - start_time}"
        )

    except Exception as e:

        print(f"Pipeline Failed: {e}")


if __name__ == "__main__":
    main()
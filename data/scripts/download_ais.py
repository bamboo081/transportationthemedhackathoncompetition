## Not necessarily needed for the script, but the functionally of this script is to download the AIS data from the NOAA website
# # and save it to a local directory. The script uses the requests library to download the data and the os library to create the directory if it doesn't exist.

# data/scripts/download_ais.py

#!/usr/bin/env python3
"""
(download_ais.py)
Placeholder script to fetch AIS CSVs from NOAA public archive.
"""

import os
import argparse
from datetime import datetime, timedelta

def parse_args():
    parser = argparse.ArgumentParser(
        description="Download AIS CSVs from NOAA (placeholder)"
    )
    parser.add_argument("--start", required=True,
                        help="Start date YYYY-MM-DD")
    parser.add_argument("--end", required=True,
                        help="End date YYYY-MM-DD")
    parser.add_argument("--output-dir", default="data/raw",
                        help="Where to save CSVs")
    return parser.parse_args()

def main():
    args = parse_args()
    os.makedirs(args.output_dir, exist_ok=True)
    # TODO: implement NOAA download logic
    start = datetime.fromisoformat(args.start)
    end = datetime.fromisoformat(args.end)
    date = start
    while date <= end:
        print(f"[placeholder] Download AIS for {date.date()}")
        # e.g. fetch URL and save as CSV
        date += timedelta(days=1)

if __name__ == "__main__":
    main()

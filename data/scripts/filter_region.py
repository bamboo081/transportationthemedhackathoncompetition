# data/scripts/filter_region.py
#!/usr/bin/env python3
"""
Filter the AIS CSV files by the Gulf of Mexico
"""
import os
import argparse
import pandas as pd
from glob import glob

def parse_args():
    parser = argparse.ArgumentParser(
        description="Filter AIS CSVs by region (Gulf of Mexico by default)"
    )
    parser.add_argument(
        "--input-dir", "-i", default="data/raw", help="Directory of raw CSVs"
    )
    parser.add_argument(
        "--output-dir", "-o", default="data/processed", help="Directory for filtered CSVs"
    )
    parser.add_argument(
        "--lat-min", type=float, default=18.0, help="Minimum latitude"
    )
    parser.add_argument(
        "--lat-max", type=float, default=31.0, help="Maximum latitude"
    )
    parser.add_argument(
        "--lon-min", type=float, default=-98.0, help="Minimum longitude"
    )
    parser.add_argument(
        "--lon-max", type=float, default=-81.0, help="Maximum longitude"
    )
    return parser.parse_args()

def filter_file(filepath, lat_min, lat_max, lon_min, lon_max):
    df = pd.read_csv(filepath, parse_dates=["BaseDateTime"])
    mask = (
        (df["LAT"] >= lat_min) & (df["LAT"] <= lat_max) &
        (df["LON"] >= lon_min) & (df["LON"] <= lon_max)
    )
    return df.loc[mask]

def main():
    args = parse_args()
    os.makedirs(args.output_dir, exist_ok=True)
    for filepath in glob(os.path.join(args.input_dir, "*.csv")):
        print(f"Filtering {filepath}")
        filtered = filter_file(
            filepath,
            args.lat_min, args.lat_max,
            args.lon_min, args.lon_max
        )
        out_path = os.path.join(args.output_dir, os.path.basename(filepath))
        filtered.to_csv(out_path, index=False)
        print(f"  → Saved to {out_path}")

if __name__ == "__main__":
    main()

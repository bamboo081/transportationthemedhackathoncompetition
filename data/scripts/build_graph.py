# data/scripts/build_graph.py
#!/usr/bin/env python3
"""
Build a directed, weighted vessel-movement graph from filtered AIS data.
"""
import os
import argparse
import pandas as pd
import networkx as nx
import pickle
import math
from glob import glob

def haversine(lat1, lon1, lat2, lon2):
    R = 6371.0  # Earth radius in kilometers
    phi1, phi2 = math.radians(lat1), math.radians(lat2)
    dphi = math.radians(lat2 - lat1)
    dlambda = math.radians(lon2 - lon1)
    a = math.sin(dphi / 2)**2 + math.cos(phi1) * math.cos(phi2) * math.sin(dlambda / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return R * c

def parse_args():
    parser = argparse.ArgumentParser(
        description="Build vessel movement graph"
    )
    parser.add_argument(
        "--input-dir", "-i", default="data/processed", help="Directory of filtered CSVs"
    )
    parser.add_argument(
        "--output-graph", "-o", default="data/processed/graph.pkl", help="File to save graph"
    )
    return parser.parse_args()

def main():
    args = parse_args()
    G = nx.DiGraph()

    for filepath in glob(os.path.join(args.input_dir, "*.csv")):
        print(f"Reading {filepath}")
        df = pd.read_csv(filepath, parse_dates=["BaseDateTime"])
        df.sort_values(by=["MMSI", "BaseDateTime"], inplace=True)
        for _, vessel in df.groupby("MMSI"):
            coords = list(zip(vessel["LAT"], vessel["LON"]))
            for (lat1, lon1), (lat2, lon2) in zip(coords, coords[1:]):
                dist = haversine(lat1, lon1, lat2, lon2)
                u, v = (lat1, lon1), (lat2, lon2)
                if G.has_edge(u, v):
                    G[u][v]["distance"] += dist
                else:
                    G.add_edge(u, v, distance=dist)

    print(f"Built graph with {G.number_of_nodes()} nodes and {G.number_of_edges()} edges")
    os.makedirs(os.path.dirname(args.output_graph), exist_ok=True)
    with open(args.output_graph, "wb") as f:
        pickle.dump(G, f)
    print(f"Graph saved to {args.output_graph}")

if __name__ == "__main__":
    main()

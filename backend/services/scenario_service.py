# backend/services/scenario_service.py

import json
from pathlib import Path
from typing import Dict
import networkx as nx
from backend.config import SCENARIOS_DIR

def load_scenario(name: str) -> Dict:
    """Read scenario JSON (e.g. 'panama_drought') from scenarios/."""
    path = Path(SCENARIOS_DIR) / f"{name}.json"
    with open(path) as f:
        return json.load(f)

def apply_scenario(
    graph: nx.DiGraph,
    scenario: Dict
) -> nx.DiGraph:
    """
    Return a new graph with edge weights and node attrs adjusted by the scenario.
    - edge_capacity_factor <1 → increases weight (slower throughput)
    - node_capacity_factor just stored as node attribute
    """
    g = graph.copy()
    e_factor = scenario.get("edge_capacity_factor", 1.0)
    n_factor = scenario.get("node_capacity_factor", 1.0)

    # Increase weights inversely proportional to capacity
    def weight_fn(u, v, orig):
        return orig / e_factor

    # Apply to edges
    for u, v, data in g.edges(data=True):
        data["distance"] = weight_fn(u, v, data["distance"])

    # Tag nodes (could be used for queuing later)
    for node, data in g.nodes(data=True):
        data["capacity_factor"] = n_factor

    return g

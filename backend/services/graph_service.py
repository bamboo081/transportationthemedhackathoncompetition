# backend/services/graph_service.py

import pickle
from typing import Tuple, List
import networkx as nx
from backend.config import GRAPH_PATH

def load_graph(path: str = GRAPH_PATH) -> nx.DiGraph:
    """Load the pre-built vessel-movement graph from disk."""
    with open(path, "rb") as f:
        return pickle.load(f)

def shortest_path(
    graph: nx.DiGraph,
    source: Tuple[float, float],
    target: Tuple[float, float],
    weight: str = "distance"
) -> List[Tuple[float, float]]:
    """Compute the Dijkstra shortest path (by weight) between two coords."""
    return nx.shortest_path(graph, source, target, weight=weight)

def shortest_path_length(
    graph: nx.DiGraph,
    source: Tuple[float, float],
    target: Tuple[float, float],
    weight: str = "distance"
) -> float:
    """Compute the Dijkstra shortest-path length between two coords."""
    return nx.shortest_path_length(graph, source, target, weight=weight)

def astar_path(
    graph: nx.DiGraph,
    source: Tuple[float, float],
    target: Tuple[float, float]
) -> List[Tuple[float, float]]:
    """Compute an A* path using haversine distance as heuristic."""
    from math import radians, sin, cos, atan2, sqrt

    def haversine(u, v):
        R = 6371.0
        φ1, φ2 = radians(u[0]), radians(v[0])
        dφ = radians(v[0] - u[0])
        dλ = radians(v[1] - u[1])
        a = sin(dφ/2)**2 + cos(φ1)*cos(φ2)*sin(dλ/2)**2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))
        return R * c

    return nx.astar_path(graph, source, target, heuristic=haversine)

def apply_weight_function(
    graph: nx.DiGraph,
    fn
) -> nx.DiGraph:
    """
    Mutate all edges via fn(u, v, original_distance) → new_distance.
    Useful for scenario-based weight adjustments.
    """
    for u, v, data in graph.edges(data=True):
        data["distance"] = fn(u, v, data["distance"])
    return graph

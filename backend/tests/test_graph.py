import networkx as nx
import pytest
from backend.services.graph_service import (
    shortest_path,
    shortest_path_length,
    astar_path,
    apply_weight_function,
)

@pytest.fixture
def simple_graph():
    # Create a small directed graph:
    # (0,0) → (0,1) [dist=1]
    # (0,1) → (1,1) [dist=1]
    # (0,0) → (1,1) [dist=3]
    G = nx.DiGraph()
    G.add_edge((0, 0), (0, 1), distance=1)
    G.add_edge((0, 1), (1, 1), distance=1)
    G.add_edge((0, 0), (1, 1), distance=3)
    return G

def test_shortest_path(simple_graph):
    path = shortest_path(simple_graph, (0, 0), (1, 1))
    assert path == [(0, 0), (0, 1), (1, 1)]

def test_shortest_path_length(simple_graph):
    length = shortest_path_length(simple_graph, (0, 0), (1, 1))
    assert length == 2

def test_astar_path(simple_graph):
    path = astar_path(simple_graph, (0, 0), (1, 1))
    assert path == [(0, 0), (0, 1), (1, 1)]

def test_apply_weight_function(simple_graph):
    # Define a weight doubling function
    def double_weight(u, v, orig):
        return orig * 2
    G2 = apply_weight_function(simple_graph.copy(), double_weight)
    # Every edge's distance should be doubled
    for u, v, data in G2.edges(data=True):
        assert data["distance"] == simple_graph[u][v]["distance"] * 2

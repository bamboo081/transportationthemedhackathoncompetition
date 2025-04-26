# backend/routes/simulation.py

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from typing import Tuple, List
import networkx as nx

from backend.services.graph_service import (
    load_graph, shortest_path, shortest_path_length, astar_path
)
from backend.services.scenario_service import load_scenario, apply_scenario

router = APIRouter(tags=["simulation"])

class SimulationRequest(BaseModel):
    scenario: str
    source: Tuple[float, float] = Field(..., description="(lat, lon)")
    target: Tuple[float, float] = Field(..., description="(lat, lon)")
    algorithm: str = Field("dijkstra", description="Either 'dijkstra' or 'astar'")

class SimulationResponse(BaseModel):
    path: List[Tuple[float, float]]
    total_distance: float

@router.post("/simulate", response_model=SimulationResponse)
def simulate(req: SimulationRequest):
    # 1. Load base graph
    graph = load_graph()

    # 2. Load & apply scenario
    try:
        scenario = load_scenario(req.scenario)
    except FileNotFoundError:
        raise HTTPException(404, detail="Scenario not found")
    g2 = apply_scenario(graph, scenario)

    # 3. Compute path
    if req.algorithm.lower() == "astar":
        path = astar_path(g2, req.source, req.target)
        dist = nx.astar_path_length(g2, req.source, req.target, heuristic=None)
    else:
        path = shortest_path(g2, req.source, req.target)
        dist = shortest_path_length(g2, req.source, req.target)

    return SimulationResponse(path=path, total_distance=dist)

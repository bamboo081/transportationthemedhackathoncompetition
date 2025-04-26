# backend/config.py

from pathlib import Path

# ─── Data Paths ───────────────────────────────────────────────────────────────
RAW_DATA_DIR       = Path("data/raw")
PROCESSED_DATA_DIR = Path("data/processed")
GRAPH_PATH         = PROCESSED_DATA_DIR / "graph.pkl"
SCENARIOS_DIR      = Path("scenarios")

# ─── Geographic Defaults ──────────────────────────────────────────────────────
REGION_BOUNDS = {
    "lat_min": 18.0,
    "lat_max": 31.0,
    "lon_min": -98.0,
    "lon_max": -81.0,
}

# ─── PDF Report Settings ──────────────────────────────────────────────────────
PDF_TITLE        = "Climate Impact Report"
PDF_SUBTITLE     = "Maritime Traffic Analysis"
PDF_AUTHOR       = "LogMap 3.0"
PDF_PAGE_SIZE    = "LETTER"
PDF_MARGIN       = 50        # points
PDF_CHART_WIDTH  = 400       # pixels
PDF_CHART_HEIGHT = 200       # pixels

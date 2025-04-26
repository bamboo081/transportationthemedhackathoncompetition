# backend/services/report_service.py

import io
import tempfile
from pathlib import Path

import networkx as nx
import matplotlib.pyplot as plt
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas

from backend.config import (
    PDF_TITLE,
    PDF_SUBTITLE,
    PDF_AUTHOR,
    PDF_MARGIN,
    PDF_CHART_WIDTH,
    PDF_CHART_HEIGHT,
)
from backend.services.graph_service import load_graph


EMISSION_FACTOR = 10.0  # grams CO₂ per km (mock factor)


def _compute_emissions(graph: nx.DiGraph):
    """
    Compute total and per-edge emissions (distance * EMISSION_FACTOR).
    Returns total_co2 (kg), and list of (u, v, dist_km, co2_kg).
    """
    edge_data = []
    total = 0.0
    for u, v, data in graph.edges(data=True):
        dist = data.get("distance", 0.0)
        co2 = (dist * EMISSION_FACTOR) / 1000.0  # convert g to kg
        edge_data.append((u, v, dist, co2))
        total += co2
    # sort descending by emissions
    edge_data.sort(key=lambda x: x[3], reverse=True)
    return total, edge_data


def _make_chart(top_edges):
    """
    Generate a simple bar chart of the top-5 polluting segments.
    Returns path to a temporary PNG file.
    """
    labels = [f"{u}->{v}" for u, v, _, _ in top_edges]
    values = [co2 for _, _, _, co2 in top_edges]

    plt.figure()
    plt.bar(range(len(values)), values)
    plt.xticks(range(len(values)), labels, rotation=45, ha="right")
    plt.ylabel("CO₂ (kg)")
    plt.tight_layout()

    tmp = tempfile.NamedTemporaryFile(suffix=".png", delete=False)
    plt.savefig(tmp.name)
    plt.close()
    return tmp.name


def generate_report(region: str) -> bytes:
    """
    Generates a PDF report for the given region.
    Returns the raw PDF bytes.
    """
    graph = load_graph()
    total_co2, edge_data = _compute_emissions(graph)
    top5 = edge_data[:5]

    # create chart
    chart_path = _make_chart(top5)

    # build PDF
    buf = io.BytesIO()
    c = canvas.Canvas(buf, pagesize=LETTER)
    width, height = LETTER

    # Title
    y = height - PDF_MARGIN
    c.setFont("Helvetica-Bold", 20)
    c.drawCentredString(width / 2, y, PDF_TITLE)
    y -= 30
    c.setFont("Helvetica", 12)
    c.drawCentredString(width / 2, y, f"{PDF_SUBTITLE} — {region.capitalize()}")
    y -= 40

    # Summary
    c.setFont("Helvetica-Bold", 14)
    c.drawString(PDF_MARGIN, y, "1. Summary of CO₂ Emissions")
    y -= 20
    c.setFont("Helvetica", 12)
    c.drawString(PDF_MARGIN, y, f"Total estimated CO₂: {total_co2:.2f} kg")
    y -= 40

    # Top 5 polluting segments table
    c.setFont("Helvetica-Bold", 14)
    c.drawString(PDF_MARGIN, y, "2. Top 5 Polluting Segments")
    y -= 20
    c.setFont("Helvetica-Bold", 10)
    c.drawString(PDF_MARGIN, y, "Segment")
    c.drawString(PDF_MARGIN + 250, y, "Distance (km)")
    c.drawString(PDF_MARGIN + 350, y, "CO₂ (kg)")
    y -= 15
    c.setFont("Helvetica", 10)
    for u, v, dist, co2 in top5:
        seg = f"{u}->{v}"
        c.drawString(PDF_MARGIN, y, seg)
        c.drawRightString(PDF_MARGIN + 320, y, f"{dist:.1f}")
        c.drawRightString(PDF_MARGIN + 420, y, f"{co2:.2f}")
        y -= 15
    y -= 20

    # Chart
    c.setFont("Helvetica-Bold", 14)
    c.drawString(PDF_MARGIN, y, "3. Emissions Bar Chart")
    y -= PDF_CHART_HEIGHT + 20
    c.drawImage(chart_path, PDF_MARGIN, y, width=PDF_CHART_WIDTH, height=PDF_CHART_HEIGHT)
    y -= 30

    # Suggested green routes (placeholder)
    c.setFont("Helvetica-Bold", 14)
    c.drawString(PDF_MARGIN, y, "4. Suggested Green Routes")
    y -= 20
    c.setFont("Helvetica", 12)
    for idx, (u, v, _, _) in enumerate(top5, start=1):
        c.drawString(PDF_MARGIN, y, f"{idx}. Avoid segment {u} → {v} to reduce emissions.")
        y -= 15

    # Footer & save
    c.showPage()
    c.save()
    buf.seek(0)

    # Clean up temp chart
    try:
        Path(chart_path).unlink()
    except OSError:
        pass

    return buf.read()

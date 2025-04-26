import pytest
import networkx as nx
from backend.services.report_service import generate_report

@pytest.fixture(autouse=True)
def mock_graph(monkeypatch):
    # Build a tiny graph with one edge of 100 km
    G = nx.DiGraph()
    G.add_edge((0, 0), (0, 1), distance=100)
    # Monkey-patch load_graph so report_service uses our small graph
    import backend.services.report_service as rs
    monkeypatch.setattr(rs, "load_graph", lambda: G)
    return G

def test_generate_report_returns_pdf():
    pdf_bytes = generate_report("testregion")
    # Should be bytes and start with PDF header
    assert isinstance(pdf_bytes, (bytes, bytearray))
    assert pdf_bytes.startswith(b"%PDF")
    # Check if the PDF contains the expected content
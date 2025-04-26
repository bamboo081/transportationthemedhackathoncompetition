<!-- README.md -->

# LogMap 3.0

**Maritime Digital-Twin & Climate Impact Simulator**

**Overview**  
LogMap 3.0 ingests six days of real AIS data, filters to your region, builds a graph of vessel movements, simulates “what-if” climate scenarios, recomputes optimal reroutes, visualizes them on a Mapbox GL dashboard, and generates a printable PDF Climate Impact Report.

---

## Features

- **Data Pipeline**: Raw CSV → Region filter → NetworkX graph  
- **Simulation**: JSON-driven perturbations + Dijkstra/A* rerouting  
- **Dashboard**: Next.js + Mapbox GL with time-slider animations  
- **Reporting**: ReportLab PDF with emissions tables & charts  
- **Containerized**: Docker & docker-compose for full stack  

---



1. **Clone & preprocess data**  
   ```bash
   git clone <repo>
   cd logmap-3.0
   bash data/scripts/preprocess.sh

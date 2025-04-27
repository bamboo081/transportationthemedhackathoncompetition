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

2. **Data files**
   The data files aren't in the upload because of their size, but the site they're available from is: "https://coast.noaa.gov/htdata/CMSP/AISDataHandler/2024/index.html"
      Download the first and last days of the year and unzip them  - add them to the raw subfolder in the data folder

3. **Processing**
   The .csv files need to be processed before use - the scripts needed to run for preprocessing are:
      1. filter_region.py
      2. build_graph.py
   You must run these in the exact same order in order for the script to work. The processed data uploads to the processed subfolder in the data folder, which is used by other files in the project.
# data/scripts/preprocess.sh
#!/usr/bin/env bash
# Preprocessing pipeline: filter raw AIS data and build graph

set -eo pipefail

echo "=== Starting preprocessing ==="

python3 data/scripts/filter_region.py \
  --input-dir data/raw \
  --output-dir data/processed \
  --lat-min 18.0 --lat-max 31.0 \
  --lon-min -98.0 --lon-max -81.0

python3 data/scripts/build_graph.py \
  --input-dir data/processed \
  --output-graph data/processed/graph.pkl

echo "=== Preprocessing complete! ==="

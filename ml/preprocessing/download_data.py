from pathlib import Path
RAW_DATA_DIR=Path("data/raw/tcga_brca")
RAW_DATA_DIR.mkdir(parents=True, exist_ok=True)

print("Raw data directory ready!")
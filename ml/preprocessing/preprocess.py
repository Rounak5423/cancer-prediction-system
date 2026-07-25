from pathlib import Path
import pandas as pd 

RAW_DIR=Path("data/raw/tcga_brca")
PROCESSED_DIR=Path("data/processed")

PROCESSED_DIR.mkdir(exist_ok=True)
print("Preprocessing started...")
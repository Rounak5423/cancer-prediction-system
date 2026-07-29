from pathlib import Path
import pandas as pd

class GenomePreprocessor:

    def __init__(self):
        self.processed_data_path=Path("data/processed")

    def transpose_dataset(self,dataset):
        dataset=dataset.set_index("sample")
        dataset=dataset.T
        return dataset
    
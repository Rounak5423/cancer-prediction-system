from pathlib import Path
import pandas as pd

class DatasetLoader:
    def __init__(self):
        self.dataset_path=Path("data/raw/tcga_brca")
        self.detaset=None

    def load(self,filename):
        file=self.dataset_path/filename
        self.dataset=pd.read_csv(file)
        print("Dataset loaded successfully")
        return self.dataset

    def summary(self):
        print("shape:",self.dataset.shape)
        print()
        print(self.dataset.info())
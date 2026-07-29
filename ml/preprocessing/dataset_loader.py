from pathlib import Path
import pandas as pd

class DatasetLoader:
    def __init__(self):
        self.raw_data_path=Path("data/raw/tcga_brca")
        self.dataset=None

    def load(self,filename):
        file_path=self.raw_data_path/filename
        self.dataset=pd.read_csv(
            file_path,sep="\t"
        )
        return self.dataset

    def inspect(self):
       
        print("Dataset overview:-")

        print("\nshape:")
        print(self.dataset.shape)

        print("\ncolumns:")
        print(self.dataset.columns.tolist()[:10])

        print("\nDatatypes:")
        print(self.dataset.dtypes.head())

        print("\nMissing values")
        print(self.dataset.isnull().sum().sum())

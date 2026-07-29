import pandas as pd
from pathlib import Path


class GenomePreprocessor:
    def __init__(self):
       self.raw_data_path=Path("data/raw")
       self.processed_data_path=Path("data/processed")
       self.data=None

    def show_info(self):
        print("Genome preprocessor")
        print("Raw data:",self.raw_data_path)
        print("processed data:",self.processed_data_path)

    def load_data(self,filename):
        file_path= self.raw_data_path/filename
        self.data=pd.read_csv(file_path)
        print("Dataset loaded successfully")

    def dataset_shape(self):
        print(self.data.shape)

    def show_coloumns(self):
        print(self.data.columns)

    def missing_values(self):
        print(self.data.isnull().sum())

preprocessor=GenomePreprocessor()
preprocessor.show_info()


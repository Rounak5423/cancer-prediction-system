from pathlib import Path
import pandas as pd

class GenomePreprocessor:

    def __init__(self):
        self.processed_data_path=Path("data/processed")
        self.processed_data_path.mkdir(parents=True,exist_ok=True)

    def transpose_dataset(self,dataset):
        dataset=dataset.set_index("sample")
        dataset=dataset.T
        dataset=dataset.reset_index()
        dataset.rename(
            columns={"index" : "patient_id"}
        )
        return dataset
    def save_processed_datasets(self,dataset,filename):

        file_path=self.processed_data_path/filename
        dataset.to_csv(file_path)
        print(f"Processed dataset saved to {file_path}")

    def create_labels(self,dataset):
        labels=[]
        for patient in dataset["patient_id"]:
            sample_type = patient.split("-")[-1]

            if sample_type=="01":
                labels.append(1)
            elif sample_type=="11":
                labels.append(0)
            else:
                labels.append=None
        dataset["label"]=labels
        return dataset
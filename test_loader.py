from ml.preprocessing.preprocessor import GenomePreprocessor
from ml.preprocessing.dataset_loader import DatasetLoader
loader = DatasetLoader()

preprocessor= GenomePreprocessor()

#raw dataset

df = loader.load("d1.tsv")
print("Original shape:",df.shape)
print(df.head())
print("columns:", df.columns.tolist())

#preprocessed dataset

transposed_df=preprocessor.transpose_dataset(df)
print(transposed_df.head())
print("Processed shape",transposed_df.shape)

#save processed dataset

preprocessor.save_processed_datasets(transposed_df,"tcgra_brca_processed.csv")




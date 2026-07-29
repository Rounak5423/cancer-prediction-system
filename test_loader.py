from ml.preprocessing.preprocessor import GenomePreprocessor
from ml.preprocessing.dataset_loader import DatasetLoader
loader = DatasetLoader()
df = loader.load("d1.tsv")
preprocessor= GenomePreprocessor()
print(df.head())
print("columns:", df.columns.tolist())
transposed_df=preprocessor.transpose_dataset(df)
print(transposed_df.head())
print(transposed_df.shape)


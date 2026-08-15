from ml.preprocessing.preprocessor import GenomePreprocessor
from ml.preprocessing.dataset_loader import DatasetLoader
from ml.training.trainer import ModelTrainer

loader = DatasetLoader()
preprocessor= GenomePreprocessor()
trainer=ModelTrainer()

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

#create labels
processed_df=preprocessor.create_labels(transposed_df)
processed_df=processed_df.dropna(subset=["label"])
print("\nLAbel distribution:")
print(processed_df["label"].value_counts(dropna=False))

sample_types = transposed_df["patient_id"].str.split("-").str[-1]
print("\nSAMPLE TYPEDISTRIBUTION")
print(sample_types.value_counts())

#split into features and training
x,y=preprocessor.split_features_and_target(processed_df)
trainer=ModelTrainer()

#split into training and testing sets
x_train,x_test,y_train,y_test= trainer.split_dataset(x,y)
model=trainer.train_logistic_regression(
    x_train,
    y_train
)
print("\n model trained successfully!")

#verify
print("Training feature  :",x_train.shape)
print("Testing feature   :",x_test.shape)
print("Training label    :",y_train.shape)
print("Testing label     :",y_test.shape)






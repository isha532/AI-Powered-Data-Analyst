
import pandas as pd
from pathlib import Path

# Project folder
BASE_DIR = Path(__file__).resolve().parent

# CSV file path
DATASET_PATH = BASE_DIR / "sample_data" / "sales_data.csv"

# Read dataset
df = pd.read_csv(DATASET_PATH)

# Display dataset
print("\nDataset:")
print(df)

# Display columns
print("\nColumns:")
print(df.columns.tolist())

# Display dataset information
print("\nDataset Information:")
print(df.info())

# Display statistical summary
print("\nStatistical Summary:")
print(df.describe())

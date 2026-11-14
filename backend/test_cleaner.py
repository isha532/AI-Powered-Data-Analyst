import pandas as pd

from backend.cleaner import (
    clean_missing_values,
    remove_duplicates,
    convert_numeric_columns,
    standardize_text_columns
)

df = pd.read_csv("sample_data/sales_data.csv")

print("Original Data:")
print(df)

df = clean_missing_values(df)
df = remove_duplicates(df)
df = convert_numeric_columns(df, ["Quantity", "Price"])
df = standardize_text_columns(df, ["Product", "Category", "Region"])

print("\nCleaned Data:")
print(df)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())
from backend.data_loader import load_data

with open("sample_data/sales_data.csv", "rb") as file:
    df = load_data(file)

print("Data loaded successfully!")

print("\nFirst 5 rows:")
print(df.head())

print("\nDataset Shape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns.tolist())
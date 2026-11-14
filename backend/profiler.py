
import pandas as pd


def profile_data(df):

    if not isinstance(df, pd.DataFrame):
        raise TypeError("Input must be a Pandas DataFrame")

    if df.empty:
        raise ValueError("Dataset is empty")

    profile = {
        "total_rows": len(df),
        "total_columns": len(df.columns),
        "missing_values": df.isnull().sum().to_dict(),
        "duplicate_rows": int(df.duplicated().sum()),
        "data_types": df.dtypes.astype(str).to_dict(),
        "numerical_summary": df.describe().to_dict()
    }

    return profile

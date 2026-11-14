
import pandas as pd
from backend.cleaner import clean_missing_values


def test_clean_missing_values():

    data = {
        "Name": ["Rahul", "Priya", "Amit"],
        "Age": [22, None, 25],
        "City": ["Pune", "Nagpur", None]
    }

    df = pd.DataFrame(data)

    cleaned_df = clean_missing_values(df)

    assert cleaned_df["Age"].isnull().sum() == 0
    assert cleaned_df["City"].isnull().sum() == 0

    print("Missing values handled successfully!")


def test_original_data_unchanged():

    df = pd.DataFrame({
        "Age": [22, None, 25]
    })

    cleaned_df = clean_missing_values(df)

    assert df["Age"].isnull().sum() == 1
    assert cleaned_df["Age"].isnull().sum() == 0

from backend.cleaner import remove_duplicates


def test_remove_duplicates():

    data = {
        "Name": ["Rahul", "Priya", "Rahul"],
        "Age": [22, 24, 22]
    }

    df = pd.DataFrame(data)

    cleaned_df = remove_duplicates(df)

    assert len(cleaned_df) == 2
    assert cleaned_df.duplicated().sum() == 0


def test_original_data_unchanged_after_duplicate_removal():

    df = pd.DataFrame({
        "Name": ["Rahul", "Rahul"],
        "Age": [22, 22]
    })

    cleaned_df = remove_duplicates(df)

    assert len(df) == 2
    assert len(cleaned_df) == 1
from backend.cleaner import clean_missing_values, remove_duplicates


from backend.cleaner import convert_numeric_columns


def test_convert_numeric_columns():

    df = pd.DataFrame({
        "Age": ["22", "25", "30"],
        "Name": ["Rahul", "Priya", "Amit"]
    })

    cleaned_df = convert_numeric_columns(df, ["Age"])

    assert pd.api.types.is_numeric_dtype(cleaned_df["Age"])
    assert cleaned_df["Age"].tolist() == [22, 25, 30]


def test_invalid_values_become_missing():

    df = pd.DataFrame({
        "Age": ["22", "unknown", "30"]
    })

    cleaned_df = convert_numeric_columns(df, ["Age"])

    assert cleaned_df["Age"].isnull().sum() == 1


from backend.cleaner import standardize_text_columns


def test_standardize_text_columns():

    df = pd.DataFrame({
        "City": [" nagpur ", "PUNE", "mumbai "]
    })

    cleaned_df = standardize_text_columns(df, ["City"])

    assert cleaned_df["City"].tolist() == [
        "Nagpur",
        "Pune",
        "Mumbai"
    ]


def test_original_text_data_unchanged():

    df = pd.DataFrame({
        "City": [" nagpur "]
    })

    cleaned_df = standardize_text_columns(df, ["City"])

    assert df["City"].iloc[0] == " nagpur "
    assert cleaned_df["City"].iloc[0] == "Nagpur"

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
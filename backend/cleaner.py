
import pandas as pd


def clean_missing_values(df):

    df = df.copy()

    for column in df.columns:

        if df[column].isnull().sum() > 0:

            if df[column].dtype in ["int64", "float64"]:

                df[column] = df[column].fillna(
                    df[column].median()
                )

            else:

                df[column] = df[column].fillna(
                    df[column].mode()[0]
                )

    return df


def remove_duplicates(df):

    df = df.copy()

    df = df.drop_duplicates()

    return df

def convert_numeric_columns(df, columns):

    df = df.copy()

    for column in columns:

        df[column] = pd.to_numeric(
            df[column],
            errors="coerce"
        )

    return df


def standardize_text_columns(df, columns):

    df = df.copy()

    for column in columns:

        df[column] = (
            df[column]
            .astype("string")
            .str.strip()
            .str.title()
        )

    return df
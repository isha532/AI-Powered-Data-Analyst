
import pandas as pd


def load_data(file):
    """
    Load CSV or Excel files into a Pandas DataFrame.
    """

    try:
        file_name = file.name.lower()

        if file_name.endswith(".csv"):
            df = pd.read_csv(file)

        elif file_name.endswith((".xlsx", ".xls")):
            df = pd.read_excel(file)

        else:
            raise ValueError(
                "Unsupported file format. Please upload CSV or Excel."
            )

        if df.empty:
            raise ValueError("The uploaded file is empty.")

        return df

    except Exception as e:
        raise ValueError(f"Error loading file: {e}")

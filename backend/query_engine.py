
import pandas as pd
import sqlite3


def run_query(df, query):

    if not isinstance(df, pd.DataFrame):
        raise TypeError("Input must be a Pandas DataFrame")

    if df.empty:
        raise ValueError("Dataset is empty")

    connection = sqlite3.connect(":memory:")

    try:
        df.to_sql("sales", connection, index=False, if_exists="replace")

        result = pd.read_sql_query(query, connection)

        return result

    except Exception as e:
        raise ValueError(f"SQL Query Error: {e}")

    finally:
        connection.close()

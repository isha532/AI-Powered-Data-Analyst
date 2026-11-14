
import pandas as pd
import pytest

from backend.query_engine import run_query


def test_select_query():

    df = pd.DataFrame({
        "Product": ["Laptop", "Mobile", "Chair"],
        "Price": [50000, 15000, 3000]
    })

    result = run_query(df, "SELECT * FROM sales")

    assert len(result) == 3
    assert "Product" in result.columns
    assert "Price" in result.columns


def test_filter_query():

    df = pd.DataFrame({
        "Product": ["Laptop", "Mobile", "Chair"],
        "Price": [50000, 15000, 3000]
    })

    result = run_query(
        df,
        "SELECT * FROM sales WHERE Price > 10000"
    )

    assert len(result) == 2


def test_empty_dataframe():

    df = pd.DataFrame()

    with pytest.raises(ValueError):
        run_query(df, "SELECT * FROM sales")


def test_invalid_query():

    df = pd.DataFrame({
        "Product": ["Laptop"]
    })

    with pytest.raises(ValueError):
        run_query(df, "SELECT * FROM unknown_table")

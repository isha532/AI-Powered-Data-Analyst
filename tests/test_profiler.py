
import pandas as pd
import pytest

from backend.profiler import profile_data


def test_profile_data():

    df = pd.DataFrame({
        "Name": ["Isha", "Rahul", "Amit", "Isha"],
        "Age": [22, 23, None, 22],
        "Salary": [25000, 30000, 35000, 25000]
    })

    result = profile_data(df)

    assert result["total_rows"] == 4
    assert result["total_columns"] == 3
    assert result["duplicate_rows"] == 1

    assert result["missing_values"]["Age"] == 1

    assert "Salary" in result["numerical_summary"]


def test_empty_dataframe():

    df = pd.DataFrame()

    with pytest.raises(ValueError):
        profile_data(df)


def test_invalid_input():

    with pytest.raises(TypeError):
        profile_data("invalid data")

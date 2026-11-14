
import pytest
import pandas as pd
from backend.data_loader import load_data


def test_load_csv():
    data = "Name,Age\nIsha,22\nRahul,23"

    from io import BytesIO

    file = BytesIO(data.encode("utf-8"))
    file.name = "test.csv"

    df = load_data(file)

    assert isinstance(df, pd.DataFrame)
    assert df.shape == (2, 2)
    assert list(df.columns) == ["Name", "Age"]


def test_unsupported_file():
    from io import BytesIO

    file = BytesIO(b"sample data")
    file.name = "test.txt"

    with pytest.raises(ValueError):
        load_data(file)


def test_empty_csv():
    from io import BytesIO

    file = BytesIO(b"")
    file.name = "empty.csv"

    with pytest.raises(ValueError):
        load_data(file)


def test_load_excel():
    from io import BytesIO

    data = pd.DataFrame({
        "Name": ["Isha", "Rahul"],
        "Age": [22, 23]
    })

    file = BytesIO()

    with pd.ExcelWriter(file, engine="openpyxl") as writer:
        data.to_excel(writer, index=False)

    file.name = "test.xlsx"
    file.seek(0)

    df = load_data(file)

    assert isinstance(df, pd.DataFrame)
    assert df.shape == (2, 2)
    assert list(df.columns) == ["Name", "Age"]

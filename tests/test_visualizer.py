
import pandas as pd
import plotly.graph_objects as go

from backend.visualizer import create_bar_chart


def test_create_bar_chart():

    df = pd.DataFrame({
        "Region": ["Nagpur", "Pune", "Mumbai"],
        "Sales": [5000, 8000, 6000]
    })

    fig = create_bar_chart(df, "Region", "Sales")

    assert isinstance(fig, go.Figure)
    assert fig.layout.title.text == "Sales by Region"
    assert list(fig.data[0].x) == ["Nagpur", "Pune", "Mumbai"]
    assert list(fig.data[0].y) == [5000, 8000, 6000]



from backend.visualizer import create_pie_chart


def test_create_pie_chart():

    df = pd.DataFrame({
        "Category": [
            "Electronics",
            "Furniture",
            "Electronics",
            "Furniture",
            "Electronics"
        ]
    })

    fig = create_pie_chart(df, "Category")

    assert isinstance(fig, go.Figure)
    assert fig.layout.title.text == "Category Distribution"
    assert list(fig.data[0].labels) == [
        "Electronics",
        "Furniture"
    ]
    assert list(fig.data[0].values) == [3, 2]
from backend.visualizer import create_bar_chart, create_pie_chart


from backend.visualizer import create_line_chart


def test_create_line_chart():

    df = pd.DataFrame({
        "Month": ["Jan", "Feb", "Mar"],
        "Sales": [1000, 2000, 1500]
    })

    fig = create_line_chart(df, "Month", "Sales")

    assert isinstance(fig, go.Figure)
    assert fig.layout.title.text == "Sales Trend"
    assert list(fig.data[0].x) == ["Jan", "Feb", "Mar"]
    assert list(fig.data[0].y) == [1000, 2000, 1500]
from backend.visualizer import (
    create_bar_chart,
    create_pie_chart,
    create_line_chart
)


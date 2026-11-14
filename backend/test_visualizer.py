
import pandas as pd

from backend.visualizer import (
    create_bar_chart,
    create_pie_chart,
    create_line_chart
)

df = pd.read_csv("sample_data/sales_data.csv")

# Region-wise quantity
region_data = df.groupby("Region", as_index=False)["Quantity"].sum()

bar_fig = create_bar_chart(
    region_data,
    "Region",
    "Quantity"
)

bar_fig.show()


# Category distribution
pie_fig = create_pie_chart(
    df,
    "Category"
)

pie_fig.show()


# Date-wise quantity trend
date_data = df.groupby("Date", as_index=False)["Quantity"].sum()

line_fig = create_line_chart(
    date_data,
    "Date",
    "Quantity"
)

line_fig.show()

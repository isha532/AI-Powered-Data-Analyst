
import pandas as pd
from backend.query_engine import run_query

df = pd.read_csv("sample_data/sales_data.csv")

print("\n1. All Sales Data")

result = run_query(
    df,
    "SELECT * FROM sales"
)
print(result)


print("\n2. Region Wise Quantity")

result = run_query(
    df,
    """
    SELECT Region, SUM(Quantity) AS Total_Quantity
    FROM sales
    GROUP BY Region
    """
)
print(result)


print("\n3. Highest Priced Product")

result = run_query(
    df,
    """
    SELECT Product, Price
    FROM sales
    ORDER BY Price DESC
    LIMIT 1
    """
)
print(result)

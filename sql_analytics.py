import sqlite3
import pandas as pd

df = pd.read_csv(
    "/Users/mahi/Documents/Python projects/python-for-ai-practice/used_car_market_analysis/cleaned_car_data.csv"
)

# 2. Creating In-Memory SQLite Database
conn = sqlite3.connect(":memory:")
df.to_sql("vehicles", conn, index=False, if_exists="replace")

# 3. Brand Price Retention Ranking using Window Functions
sql_brand_rank = """
WITH BrandStats AS (
    SELECT 
        Brand,
        COUNT(*) AS Total_Units,
        ROUND(AVG(Price), 2) AS Avg_Price,
        ROUND(AVG(Vehicle_Age), 1) AS Avg_Age,
        ROUND(AVG(Price / Vehicle_Age), 2) AS Annual_Value_Retention
    FROM vehicles
    GROUP BY Brand
)
SELECT 
    Brand,
    Total_Units,
    Avg_Price,
    Avg_Age,
    Annual_Value_Retention,
    DENSE_RANK() OVER (ORDER BY Avg_Price DESC) AS Price_Rank
FROM BrandStats;
"""
df_brand_rank = pd.read_sql_query(sql_brand_rank, conn)
print("--- Brand Value Retention Ranking ---")
print(df_brand_rank)

# 4. Fuel Type & Condition Matrix
sql_fuel_matrix = """
SELECT 
    Fuel_Type,
    Condition,
    COUNT(*) AS Unit_Count,
    ROUND(AVG(Price), 2) AS Avg_Price,
    ROUND(AVG(Mileage), 0) AS Avg_Mileage
FROM vehicles
GROUP BY Fuel_Type, Condition
ORDER BY Fuel_Type, Avg_Price DESC;
"""
df_fuel_matrix = pd.read_sql_query(sql_fuel_matrix, conn)

conn.close()

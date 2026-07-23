import pandas as pd
import numpy as np

# 1. Loading Raw Data
raw_df = pd.read_csv(
    "/Users/mahi/Documents/Python projects/python-for-ai-practice/used_car_market_analysis/car_price_prediction_.csv"
)

# 2. Feature Engineering
# Calculating Vehicle Age based on current year
CURRENT_YEAR = 2026
raw_df["Vehicle_Age"] = CURRENT_YEAR - raw_df["Year"]

# Annual usage metric (prevent division by zero for new cars)
raw_df["Mileage_Per_Year"] = (
    raw_df["Mileage"] / np.maximum(raw_df["Vehicle_Age"], 1)
).round(2)

# Price Tiers (Quantile-based: Budget, Mid-Range, Premium)
raw_df["Price_Tier"] = pd.qcut(
    raw_df["Price"], q=3, labels=["Budget", "Mid-Range", "Premium"]
)

# Mileage Brackets
mileage_bins = [0, 50000, 100000, 150000, 200000, 300000]
mileage_labels = ["<50k", "50k-100k", "100k-150k", "150k-200k", "200k+"]
raw_df["Mileage_Bracket"] = pd.cut(
    raw_df["Mileage"], bins=mileage_bins, labels=mileage_labels
)

# Clean column formatting
raw_df.columns = [col.replace(" ", "_") for col in raw_df.columns]

# 3. Export Clean Data
raw_df.to_csv(
    "/Users/mahi/Documents/Python projects/python-for-ai-practice/used_car_market_analysis/cleaned_car_data.csv",
    index=False,
)
print("Data cleaning complete. Output saved to data/cleaned_car_data.csv")

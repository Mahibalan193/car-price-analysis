import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(
    "/Users/mahi/Documents/Python projects/python-for-ai-practice/used_car_market_analysis/cleaned_car_data.csv"
)

# Set aesthetic style
sns.set_theme(style="whitegrid")
plt.rcParams["font.family"] = "sans-serif"

# 1. Price vs Mileage by Fuel Type (Scatter + Regression)
plt.figure(figsize=(10, 6))
sns.scatterplot(
    data=df, x="Mileage", y="Price", hue="Fuel_Type", alpha=0.6, palette="Set2"
)
plt.title("Vehicle Price vs. Mileage by Fuel Type", fontsize=14, fontweight="bold")
plt.xlabel("Mileage (Miles)", fontsize=12)
plt.ylabel("Price ($)", fontsize=12)
plt.savefig(
    "/Users/mahi/Documents/Python projects/python-for-ai-practice/used_car_market_analysis/price_vs_mileage.png",
    bbox_inches="tight",
)
plt.show()

# 2. Average Price by Brand & Condition (Bar Chart)
plt.figure(figsize=(12, 6))
sns.barplot(data=df, x="Brand", y="Price", hue="Condition", palette="Blues_d", ci=None)
plt.title(
    "Average Vehicle Valuation by Brand & Condition", fontsize=14, fontweight="bold"
)
plt.xlabel("Manufacturer Brand", fontsize=12)
plt.ylabel("Average Price ($)", fontsize=12)
plt.legend(title="Condition")
plt.savefig(
    "/Users/mahi/Documents/Python projects/python-for-ai-practice/used_car_market_analysis/brand_condition_valuation.png",
    bbox_inches="tight",
)
plt.show()

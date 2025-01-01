import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



df = pd.read_csv("taxi_trip_pricing.csv.csv")
df = df.dropna()
sorted_trip_price = df['Trip_Price'].dropna().sort_values().reset_index(drop=True)
plt.figure(figsize=(10, 6))
plt.plot(sorted_trip_price, color='red', linewidth=2, label='Trip Price')
plt.title("Line Graph of Trip Prices", fontsize=16)
plt.xlabel("Index (Sorted by Price)", fontsize=12)
plt.ylabel("Trip Price", fontsize=12)
plt.grid(alpha=0.3)
plt.legend()
plt.show()

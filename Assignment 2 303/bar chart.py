import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



df = pd.read_csv("taxi_trip_pricing.csv.csv")
df = df.dropna()
passenger_count_freq = df['Passenger_Count'].value_counts()
plt.figure(figsize=(8, 6))
passenger_count_freq.plot.bar(
    color=['green', 'blue', 'lime', 'orange'],
    edgecolor='black',
    width=0.7
)
plt.title("Bar Chart of Passenger Count", fontsize=16)
plt.xlabel("Number of Passengers", fontsize=12)
plt.ylabel("Frequency", fontsize=12)
plt.xticks(rotation=0)
plt.grid(axis='y', alpha=0.3)
plt.show()

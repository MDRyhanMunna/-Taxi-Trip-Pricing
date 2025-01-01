import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("taxi_trip_pricing.csv.csv")
df = df.dropna()
numeric_df = df.select_dtypes(include=['float', 'int'])

plt.figure(figsize=(8, 5))
correlation_matrix = numeric_df.corr() 
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
plt.title("Correlation Heatmap")
plt.show()


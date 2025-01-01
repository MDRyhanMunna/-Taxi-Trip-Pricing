import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("taxi_trip_pricing.csv.csv")
df = df.dropna()
time_of_day_freq = df['Time_of_Day'].value_counts()
plt.figure(figsize=(8, 6))
time_of_day_freq.plot.pie(
    autopct='%1.1f%%',  
    startangle=90,      
    colors=['green', 'blue', 'red', 'orange'],  
    explode=[0.1 if i == time_of_day_freq.idxmax() else 0 for i in time_of_day_freq.index], 
    shadow=True   
)
plt.title("Distribution of 'Time_of_Day'")
plt.ylabel('')
plt.show()
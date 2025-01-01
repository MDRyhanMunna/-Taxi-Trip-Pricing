import pandas as pd
import matplotlib.pyplot as plt



df = pd.read_csv("taxi_trip_pricing.csv.csv")
df = df.dropna()
print("For Trip_Distance_km column")
print("Mean: ", df['Trip_Distance_km'].mean())
print("Median: ", df['Trip_Distance_km'].median())
print("Variance: ", df['Trip_Distance_km'].var())
print("Standard Deviation: ", df['Trip_Distance_km'].std())
print("\n")


print("For Passenger_Count column")
print("Mean: ", df['Passenger_Count'].mean())
print("Median: ", df['Per_Km_Rate'].median())
print("Variance: ", df['Per_Km_Rate'].var())
print("Standard Deviation: ", df['Per_Km_Rate'].std())
print("\n")


print("For Base_Fare column")
print("Mean: ", df['Base_Fare'].mean())
print("Median: ", df['Base_Fare'].median())
print("Variance: ", df['Base_Fare'].var())
print("Standard Deviation: ", df['Base_Fare'].std())
print("\n")


print("For Per_Km_Rate column")
print("Mean: ", df['Per_Km_Rate'].mean())
print("Median: ", df['Per_Km_Rate'].median())
print("Variance: ", df['Per_Km_Rate'].var())
print("Standard Deviation: ", df['Per_Km_Rate'].std())
print("\n")


print("For Per_Minute_Rate column")
print("Mean: ", df['Per_Minute_Rate'].mean())
print("Median: ", df['Per_Minute_Rate'].median())
print("Variance: ", df['Per_Minute_Rate'].var())
print("Standard Deviation: ", df['Per_Minute_Rate'].std())
print("\n")


print("For Trip_Duration_Minutes column")
print("Mean: ", df['Trip_Duration_Minutes'].mean())
print("Median: ", df['Trip_Duration_Minutes'].median())
print("Variance: ", df['Trip_Duration_Minutes'].var())
print("Standard Deviation: ", df['Trip_Duration_Minutes'].std())
print("\n")


print("For Trip_Price column")
print("Mean: ", df['Trip_Price'].mean())
print("Median: ", df['Trip_Price'].median())
print("Variance: ", df['Trip_Price'].var())
print("Standard Deviation: ", df['Trip_Price'].std())
print("\n")



print("Analysis for 'Time_of_Day':")
frequency = df['Time_of_Day'].value_counts()
percentage = df['Time_of_Day'].value_counts(normalize=True) * 100
Time_of_day_analysis = pd.DataFrame({ "Frequency": frequency, "Percentage (%)": percentage})
print(Time_of_day_analysis)
print("\n")


print("Analysis for 'Day_of_Week':")
frequency = df['Day_of_Week'].value_counts()
percentage = df['Day_of_Week'].value_counts(normalize=True) * 100
Day_of_Week_analysis = pd.DataFrame({ "Frequency": frequency, "Percentage (%)": percentage})
print(Day_of_Week_analysis)
print("\n")


print("Analysis for 'Traffic_Conditions':")
frequency = df['Traffic_Conditions'].value_counts()
percentage = df['Traffic_Conditions'].value_counts(normalize=True) * 100
Traffic_Conditions_analysis = pd.DataFrame({ "Frequency": frequency, "Percentage (%)": percentage})
print(Traffic_Conditions_analysis)
print("\n")


print("Analysis for 'Weather':")
frequency = df['Weather'].value_counts()
percentage = df['Weather'].value_counts(normalize=True) * 100
Weather_analysis = pd.DataFrame({ "Frequency": frequency, "Percentage (%)": percentage})
print(Weather_analysis)
print("\n")


import pandas as pd


# Example dataset
df = pd.DataFrame({'Time_of_Day': ['Morning', 'Afternoon', 'Evening', 'Morning']})

# Apply one-hot encoding
one_hot_encoded = pd.get_dummies(df['Time_of_Day'], prefix='Time_of_Day')

# Convert boolean True/False to integers (0/1)
one_hot_encoded = one_hot_encoded.astype(int)

print(one_hot_encoded)


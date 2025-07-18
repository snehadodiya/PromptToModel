import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("dataset.csv")

 # Replace NaN values with appropriate values
df['Manufacture Date\r'].fillna(df['Manufacture Date\r'].mean(), inplace=True)

# Convert 'Manufacture Date' column to datetime format
df['Manufacture Date\r'] = pd.to_datetime(df['Manufacture Date\r'])

# Drop rows with missing values
df.dropna(inplace=True)

# Convert 'Price' and 'Kms Driven' columns to numeric types
df[['Price', 'Kms Driven']] = df[['Price', 'Kms Driven']].apply(pd.to_numeric)

# Replace 'Price' outliers with the median price
Q1 = df['Price'].quantile(0.25)
Q3 = df['Price'].quantile(0.75)
IQR = Q3 - Q1
df['Price'] = df['Price'].apply(lambda x: Q1 if x < Q1-1.5*IQR else x)
df['Price'] = df['Price'].apply(lambda x: Q3 if x > Q3+1.5*IQR else x)

# Replace 'Kms Driven' outliers with the median Kms Driven
Q1 = df['Kms Driven'].quantile(0.25)
Q3 = df['Kms Driven'].quantile(0.75)
IQR = Q3 - Q1
df['Kms Driven'] = df['Kms Driven'].apply(lambda x: Q1 if x < Q1-1.5*IQR else x)
df['Kms Driven'] = df['Kms Driven'].apply(lambda x: Q3 if x > Q3+1.5*IQR else x)

# Save the cleaned dataframe to a new csv file
df.to_csv("cleaned_df.csv", index=False)

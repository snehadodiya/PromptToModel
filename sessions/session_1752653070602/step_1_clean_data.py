 # Import necessary libraries
import pandas as pd
import numpy as np

# Assume the dataset is already loaded into a pandas DataFrame named 'df'

# Clean 'Price' column
df['Price'] = df['Price'].str.replace(',', '').astype(float)

# Replace missing values in 'Kms Driven' column with the mean of the column
df['Kms Driven'] = df['Kms Driven'].fillna(df['Kms Driven'].mean())

# Replace missing values in 'Fuel Type', 'Transmission', 'Ownership', and 'Manufacturer' columns with the mode of the columns
df[['Fuel Type', 'Transmission', 'Ownership']] = df[['Fuel Type', 'Transmission', 'Ownership']].fillna(df[['Fuel Type', 'Transmission', 'Ownership']].mode().iloc[0])

# Replace missing values in 'Manufacturer' column with the mode of the column
df['Manufacturer'] = df['Manufacturer'].fillna(df['Manufacturer'].mode().iloc[0])

# Replace missing values in 'Engine' column with the median of the column
df['Engine'] = df['Engine'].fillna(df['Engine'].median())

# Replace missing values in 'Seats' column with the median of the column
df['Seats'] = df['Seats'].fillna(df['Seats'].median())

# Clean 'Manufacture Date' column
df['Manufacture Date'] = pd.to_datetime(df['Manufacture Date'], format='%Y-%m-%d', errors='coerce')

# Drop rows with missing values in 'Manufacture Date' column
df = df.dropna(subset=['Manufacture Date'])

# Print the cleaned DataFrame
print(df)

 # Import necessary libraries
import pandas as pd
import numpy as np

# Assume 'df' is the DataFrame that contains the dataset

# Remove any rows with missing values
df = df.dropna()

# Convert 'Manufacture Date' column to datetime format
df['Manufacture Date'] = pd.to_datetime(df['Manufacture Date'], format='%Y-%m')

# Replace any empty values in 'Fuel Type' column with 'Not Specified'
df['Fuel Type'].fillna('Not Specified', inplace=True)

# Replace any empty values in 'Transmission' column with 'Not Specified'
df['Transmission'].fillna('Not Specified', inplace=True)

# Replace any empty values in 'Ownership' column with 'Not Specified'
df['Ownership'].fillna('Not Specified', inplace=True)

# Replace any empty values in 'Manufacturer' column with 'Not Specified'
df['Manufacturer'].fillna('Not Specified', inplace=True)

# Replace any empty values in 'Engine' column with 'Not Specified'
df['Engine'].fillna('Not Specified', inplace=True)

# Replace any empty values in 'Seats' column with the mean value of the column
df['Seats'].fillna(df['Seats'].mean(), inplace=True)

# Re-assign the DataFrame with the cleaned data
df = df.reset_index(drop=True)

# Print the cleaned DataFrame
print(df.head())

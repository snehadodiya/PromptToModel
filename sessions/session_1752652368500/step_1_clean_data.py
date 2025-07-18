 # Import necessary libraries
import pandas as pd
import numpy as np

# Assume 'df' is the DataFrame that contains the dataset

# Remove any missing values (na) from the DataFrame
df_clean = df.dropna()

# Remove any duplicated rows from the DataFrame
df_clean = df_clean.drop_duplicates()

# Convert 'Manufacture Date' column to datetime format
df_clean['Manufacture Date'] = pd.to_datetime(df_clean['Manufacture Date'], format='%Y-%m-%d')

# Convert 'Price' column to float type
df_clean['Price'] = pd.to_numeric(df_clean['Price'], downcast='float')

# Convert 'Kms Driven' column to int type
df_clean['Kms Driven'] = pd.to_numeric(df_clean['Kms Driven'], downcast='integer')

# Replace any non-numeric values in 'Seats' column with NaN
df_clean['Seats'] = df_clean['Seats'].replace({r'\D+': np.nan}, regex=True)

# Convert 'Seats' column to int type
df_clean['Seats'] = pd.to_numeric(df_clean['Seats'], downcast='integer')

# Print the cleaned DataFrame
print(df_clean)

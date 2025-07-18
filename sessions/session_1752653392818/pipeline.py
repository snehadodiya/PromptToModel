import pandas as pd

df = pd.read_csv('dataset.csv')


# ---- step_1_clean_data.py ----
 # Import necessary libraries
import pandas as pd
import numpy as np

# Assuming the dataset is already loaded into a pandas DataFrame named 'df'

# Remove any missing values (NaNs) from the dataset
df_clean = df.dropna()

# Convert 'Manufacture Date' column to datetime format
df_clean['Manufacture Date'] = pd.to_datetime(df_clean['Manufacture Date'])

# Replace 'NA' values in 'Fuel Type' column with NaN
df_clean['Fuel Type'] = df_clean['Fuel Type'].replace('NA', np.nan)

# Fill missing values in 'Fuel Type' column with the most common fuel type
most_common_fuel_type = df_clean['Fuel Type'].value_counts().index[0]
df_clean['Fuel Type'].fillna(most_common_fuel_type, inplace=True)

# Replace 'Manual' and 'Automatic' values in 'Transmission' column with 'Manual' and 'Automatic' respectively
df_clean['Transmission'] = df_clean['Transmission'].replace(['Manual', 'Automatic'], ['Manual', 'Automatic'])

# Convert 'Price' column to float type
df_clean['Price'] = pd.to_numeric(df_clean['Price'], errors='coerce')

# Convert 'Kms Driven' column to integer type
df_clean['Kms Driven'] = df_clean['Kms Driven'].astype(int)

# Convert 'Seats' column to integer type
df_clean['Seats'] = df_clean['Seats'].astype(int)

# Convert 'Engine' column to float type
df_clean['Engine'] = pd.to_numeric(df_clean['Engine'], errors='coerce')

# Print the cleaned dataset
print(df_clean.head())

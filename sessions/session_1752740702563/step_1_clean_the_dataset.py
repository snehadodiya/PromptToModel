import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("dataset.csv")

 ```python
# Step 1: Drop empty columns
df.drop('Unnamed: 9', axis=1, inplace=True)

# Step 2: Convert 'Price' to numeric
df['Price'] = df['Price'].replace({r'[^\d.]': '', ' thousand': 'e3', ' crore': 'e7'}, regex=True).astype(float)

# Step 3: Convert 'Kms Driven' to numeric
df['Kms Driven'] = df['Kms Driven'].str.replace('km', '').astype(float)

# Step 4: Remove 'cc' from 'Engine'
df['Engine'] = df['Engine'].str.replace('cc', '').astype(float)

# Step 5: Convert 'Seats' to integer
df['Seats'] = df['Seats'].astype(int)

# Step 6: Strip and lowercase string columns
string_cols = ['Car Name', 'Manufacturer', 'Fuel Type', 'Transmission', 'Ownership']
df[string_cols] = df[string_cols].apply(lambda col: col.str.strip().str.lower())

# Step 7: Fill missing numeric values with the mean
numeric_cols = ['Price', 'Kms Driven', 'Engine', 'Seats']
df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())

# Step 8: Fill missing categorical values with the mode
categorical_cols = ['Manufacturer', 'Fuel Type', 'Transmission', 'Ownership']
df[categorical_cols] = df[categorical_cols].fillna(df[categorical_cols].mode().iloc[0])
```

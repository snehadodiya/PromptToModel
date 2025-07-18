import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("dataset.csv")

 # Remove rows with missing values
df = df.dropna()

# Convert 'Manufacture Date' column to datetime format
df['Manufacture Date'] = pd.to_datetime(df['Manufacture Date'])

# Create a new column 'Age' by subtracting the manufacture date from today
todays_date = pd.Timestamp('2022-04-12')
df['Age'] = (todays_date - df['Manufacture Date']).dt.days

# Convert 'Price' column to numeric type
df['Price'] = pd.to_numeric(df['Price'])

# Replace any non-numeric values in 'Kms Driven' with NaN and then drop rows with NaN values
df['Kms Driven'] = pd.to_numeric(df['Kms Driven'], errors='coerce')
df = df.dropna(subset=['Kms Driven'])

# Replace 'Yes' and 'No' values in 'Transmission' column with 'Manual' and 'Automatic' respectively
df['Transmission'] = df['Transmission'].replace({'Yes': 'Manual', 'No': 'Automatic'})

# Replace 'Yes' and 'No' values in 'Ownership' column with 'First' and 'Second' respectively
df['Ownership'] = df['Ownership'].replace({'Yes': 'First', 'No': 'Second'})

# Save cleaned data to a file
df.to_csv("cleaned_data.csv", index=False)

with open("output_step_1.txt", "w") as f:
    f.write("Cleaned data saved to 'cleaned_data.csv'\n")
    f.write(df.head().to_string())

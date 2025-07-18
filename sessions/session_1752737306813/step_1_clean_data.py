import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("dataset.csv")

 # Remove rows with missing values
df = df.dropna()

# Convert 'Manufacture Date' column to datetime format
df['Manufacture Date'] = pd.to_datetime(df['Manufacture Date'])

# Create a new column 'Age' by subtracting the manufacture date from today
today = pd.Timestamp('now')
df['Age'] = today.year - df['Manufacture Date'].dt.year - ((today.month, today.day) < ('Manufacture Date'.dt.month, 'Manufacture Date'.dt.day))

# Remove 'Manufacture Date' column
df = df.drop(columns=['Manufacture Date'])

# Convert 'Price' and 'Kms Driven' columns to numeric types
df[['Price', 'Kms Driven']] = df[['Price', 'Kms Driven']].apply(pd.to_numeric)

# Replace 'Unknown' values in 'Fuel Type' column with 'Petrol'
df['Fuel Type'] = df['Fuel Type'].replace('Unknown', 'Petrol')

# Replace 'Unknown' values in 'Transmission' column with 'Manual'
df['Transmission'] = df['Transmission'].replace('Unknown', 'Manual')

# Replace 'NaN' values in 'Ownership' column with 'First Owner'
df['Ownership'] = df['Ownership'].replace('NaN', 'First Owner')

# Save the cleaned DataFrame as a CSV file
df.to_csv("cleaned_data.csv", index=False)

with open("output_step_1.txt", "w") as f:
    f.write("Cleaned data saved to 'cleaned_data.csv'")

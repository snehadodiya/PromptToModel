import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("dataset.csv")

 # Replace any null or NaN values with "not available" in the object/string columns
df = df.fillna({col: "not available" for col in df.select_dtypes(include="object").columns})

# Replace any null or NaN values with the mean of the column for numeric columns except 'Price'
df.drop('Price', axis=1, inplace=True)
df = df.fillna({col: df[col].mean() for col in df.select_dtypes(include="number").columns})
df["Price"] = df["Price"].fillna(df["Price"].mean())

# Convert 'Manufacture Date' column to datetime
df["Manufacture Date"] = pd.to_datetime(df["Manufacture Date"], format="%Y-%m-%d")

# Save the cleaned DataFrame as a csv file
df.to_csv("cleaned_data.csv", index=False)

# Save the cleaned DataFrame summary
with open("output_step_1.txt", "w") as f:
    f.write(df.head().to_string())

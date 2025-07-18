import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("dataset.csv")

 ```python
# Replace any null or NaN values in the DataFrame with the mean of the column
df = df.fillna(df.mean())

# Convert the 'Manufacture Date' column to datetime format
df['Manufacture Date'] = pd.to_datetime(df['Manufacture Date'])

# Create a new column 'Age' by subtracting the 'Manufacture Date' from the current date
df['Age'] = (pd.to_datetime('2022-04-01') - df['Manufacture Date']).dt.days // 365

# Remove the 'Manufacture Date' column as it's no longer needed
df = df.drop(columns=['Manufacture Date'])

# Save the cleaned DataFrame to a text file
with open("output_step_1.txt", "w") as f:
    f.write(df.to_string())
```

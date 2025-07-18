 # Replace NaN values with appropriate values
df['Manufacture Date\r'].fillna(df['Manufacture Date\r'].mean(), inplace=True)

# Convert 'Manufacture Date' column to datetime format
df['Manufacture Date\r'] = pd.to_datetime(df['Manufacture Date\r'])

# Drop rows with missing values
df.dropna(inplace=True)

# Convert 'Price' column to float type
df['Price'] = df['Price'].astype(float)

# Convert 'Kms Driven' column to int type
df['Kms Driven'] = df['Kms Driven'].astype(int)

# Convert 'Seats' column to int type
df['Seats'] = df['Seats'].astype(int)

# Save the cleaned dataframe as a csv file
df.to_csv("cleaned_data.csv", index=False)

with open("output_step_1.txt", "w") as f:
    f.write("Cleaned data saved as 'cleaned_data.csv'\n")
    f.write(df.head().to_string())

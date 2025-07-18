 # Remove rows with missing values
df = df.dropna()

# Convert 'Manufacture Date' column to datetime format
df['Manufacture Date'] = pd.to_datetime(df['Manufacture Date'])

# Create a new column 'Age' to calculate car age at the time of observation
df['Age'] = (pd.to_datetime('2022-04-01') - df['Manufacture Date']).dt.days / 365

# Remove 'Manufacture Date' column as it's no longer needed
df = df.drop(columns='Manufacture Date')

# Convert 'Price' column to numeric format
df['Price'] = pd.to_numeric(df['Price'])

# Convert 'Kms Driven' column to numeric format
df['Kms Driven'] = pd.to_numeric(df['Kms Driven'])

# Save the cleaned DataFrame as a csv file
df.to_csv("cleaned_data.csv", index=False)

with open("output_step_1.txt", "w") as f:
    f.write("Cleaned data has been saved as 'cleaned_data.csv'")

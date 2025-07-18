 # Remove rows with missing values
df = df.dropna()

# Convert 'Manufacture Date' column to datetime
df['Manufacture Date'] = pd.to_datetime(df['Manufacture Date'])

# Create a new column for age of the car
df['Age'] = (pd.to_datetime('2022-04-01') - df['Manufacture Date']).dt.days / 365

# Remove 'Manufacture Date' column as it's no longer needed
df = df.drop('Manufacture Date', axis=1)

# Convert 'Price' column to numeric
df['Price'] = pd.to_numeric(df['Price'])

# Convert 'Kms Driven' column to numeric
df['Kms Driven'] = pd.to_numeric(df['Kms Driven'])

# Replace any non-numeric values in 'Kms Driven' with NaN and drop those rows
df = df.replace('\\D+', np.nan, regex=True).dropna()

# Replace 'Diesel' and 'Petrol' values in 'Fuel Type' with 0 and 1 respectively
df['Fuel Type'] = df['Fuel Type'].replace({'Diesel': 0, 'Petrol': 1})

# Replace 'Manual' and 'Automatic' values in 'Transmission' with 0 and 1 respectively
df['Transmission'] = df['Transmission'].replace({'Manual': 0, 'Automatic': 1})

# Replace 'First Owner' and 'Second Owner' values in 'Ownership' with 0 and 1 respectively
df['Ownership'] = df['Ownership'].replace({'First Owner': 0, 'Second Owner': 1})

# Save the cleaned dataset as a csv file
df.to_csv("output_step_1.csv", index=False)

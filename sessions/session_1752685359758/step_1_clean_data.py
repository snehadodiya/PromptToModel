 # Replace NaN values with appropriate substitutes
df['Manufacture Date'].fillna(df['Manufacture Date'].mean(), inplace=True)
df.dropna(subset=['Price', 'Kms Driven', 'Engine', 'Seats'], inplace=True)

# Convert 'Manufacture Date' to datetime format
df['Manufacture Date'] = pd.to_datetime(df['Manufacture Date'])

# Convert 'Price' and 'Kms Driven' to float type
df[['Price', 'Kms Driven']] = df[['Price', 'Kms Driven']].astype(float)

# Convert 'Fuel Type', 'Transmission', 'Ownership', and 'Manufacturer' to categorical type
df[['Fuel Type', 'Transmission', 'Ownership', 'Manufacturer']] = df[['Fuel Type', 'Transmission', 'Ownership', 'Manufacturer']].astype('category')

# Save the cleaned dataframe to a text file
with open("output_step_1.txt", "w") as f:
    f.write(df.to_string())

# Save the cleaned dataframe to a csv file
df.to_csv("output_step_1.csv", index=False)

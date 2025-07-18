 # Remove rows with missing values
df = df.dropna()

# Convert 'Manufacture Date' column to datetime format
df['Manufacture Date'] = pd.to_datetime(df['Manufacture Date'])

# Create a new column 'Age' to represent the age of the car based on the manufacturing date
df['Age'] = (pd.Timestamp('now') - df['Manufacture Date']).dt.days / 365

# Remove the 'Manufacture Date' column as it's no longer needed
df = df.drop(columns=['Manufacture Date'])

# Convert 'Price' column to numeric type
df['Price'] = pd.to_numeric(df['Price'])

# Replace any non-numeric values in 'Kms Driven' column with NaN and then drop those rows
df['Kms Driven'] = pd.to_numeric(df['Kms Driven'], errors='coerce')
df = df.dropna(subset=['Kms Driven'])

# Replace 'Yes' and 'No' values in 'Transmission' column with 1 and 0 respectively
df['Transmission'] = df['Transmission'].map({'Yes': 1, 'No': 0})

# Replace 'Petrol', 'Diesel', 'Electric' values in 'Fuel Type' column with 0, 1, 2 respectively
df['Fuel Type'] = df['Fuel Type'].map({'Petrol': 0, 'Diesel': 1, 'Electric': 2})

# Replace 'New', 'Used' values in 'Ownership' column with 0 and 1 respectively
df['Ownership'] = df['Ownership'].map({'New': 0, 'Used': 1})

# Save the cleaned DataFrame as a csv file
df.to_csv("cleaned_data.csv", index=False)

with open("output_step_1.txt", "w") as f:
    f.write("Cleaned data has been saved as 'cleaned_data.csv'")

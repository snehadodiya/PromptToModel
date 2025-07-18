 # Remove rows with missing values
df = df.dropna()

# Convert 'Manufacture Date' column to datetime format
df['Manufacture Date'] = pd.to_datetime(df['Manufacture Date'])

# Create a new column 'Age' to store car ages
df['Age'] = (pd.DateTimeIndex(df['Manufacture Date']).year - 2022) * -1

# Convert 'Price' column to numeric type
df['Price'] = pd.to_numeric(df['Price'])

# Replace 'Kms Driven' values greater than 500000 with the mean value
mean_kms = df['Kms Driven'].mean()
df.loc[df['Kms Driven'] > 500000, 'Kms Driven'] = mean_kms

# Replace 'Price' values greater than 5000000 with the mean price
mean_price = df['Price'].mean()
df.loc[df['Price'] > 5000000, 'Price'] = mean_price

# Save the cleaned DataFrame as a csv file
df.to_csv("cleaned_data.csv", index=False)

with open("output_step_1.txt", "w") as f:
    f.write("Cleaned DataFrame saved as cleaned_data.csv\n")
    f.write(f"Number of rows before cleaning: {len(df.shape[0])}\n")
    f.write(f"Number of rows after cleaning: {df.shape[0]}\n")

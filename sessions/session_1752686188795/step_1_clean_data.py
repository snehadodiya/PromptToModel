 # Remove rows with missing values
df = df.dropna()

# Convert 'Manufacture Date' column to datetime format
df['Manufacture Date'] = pd.to_datetime(df['Manufacture Date'])

# Create a new column for age of the car
df['Age'] = (pd.to_datetime('2022-04-01') - df['Manufacture Date']).dt.days / 365

# Remove '\r' character from 'Manufacture Date'
df['Manufacture Date'] = df['Manufacture Date'].str.replace('\r', '')

# Convert 'Price' column to numeric type
df['Price'] = pd.to_numeric(df['Price'])

# Convert 'Kms Driven' column to numeric type
df['Kms Driven'] = pd.to_numeric(df['Kms Driven'])

# Remove '$' character from 'Price'
df['Price'] = df['Price'].str.replace('$', '')

# Remove ',' character from 'Price'
df['Price'] = df['Price'].str.replace(',', '')

# Save cleaned data to a text file
with open("output_step_1.txt", "w") as f:
    f.write(df.to_string())

plt.savefig("output_step_cleaned_data.png")  # Not applicable, as no plot is generated.

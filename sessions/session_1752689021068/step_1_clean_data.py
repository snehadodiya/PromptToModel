 # Remove rows with missing values
df = df.dropna()

# Convert 'Manufacture Date' column to datetime format
df['Manufacture Date'] = pd.to_datetime(df['Manufacture Date'])

# Create a new column 'Age' to store the age of the car based on the manufacture date
df['Age'] = (pd.Timestamp('now') - df['Manufacture Date']).dt.days // 365

# Remove the 'Manufacture Date' column as it's not needed anymore
df = df.drop('Manufacture Date', axis=1)

# Convert 'Price' column to numeric type
df['Price'] = pd.to_numeric(df['Price'])

# Convert 'Kms Driven' column to numeric type
df['Kms Driven'] = pd.to_numeric(df['Kms Driven'])

# Save the cleaned DataFrame as a text file
with open("output_step_1.txt", "w") as f:
    f.write(df.to_string())

# Save a plot of the data distribution
df.hist(bins=50, figsize=(20,15));
plt.savefig("output_step_1.png")

 # Remove rows with missing values
df = df.dropna()

# Convert 'Manufacture Date' column to datetime format
df['Manufacture Date'] = pd.to_datetime(df['Manufacture Date'])

# Create a new column 'Age' by subtracting the manufacture date from today
today = pd.Timestamp('now')
df['Age'] = (today - df['Manufacture Date']).dt.days // 365

# Remove the 'Manufacture Date' column as it's no longer needed
df = df.drop(columns=['Manufacture Date'])

# Convert 'Price' column to numeric type
df['Price'] = pd.to_numeric(df['Price'])

# Replace any non-numeric values in 'Kms Driven' column with NaN
df['Kms Driven'] = df['Kms Driven'].replace({' miles': np.nan}, regex=True)
# Convert 'Kms Driven' column to float type
df['Kms Driven'] = pd.to_numeric(df['Kms Driven'], errors='coerce')

# Save cleaned data to a file
df.to_csv("cleaned_data.csv", index=False)

with open("output_step_1.txt", "w") as f:
    f.write("Cleaned data saved to cleaned_data.csv\n")
    f.write(f"Number of rows before cleaning: {len(df)}\n")
    f.write(f"Number of rows after cleaning: {df.shape[0]}\n")

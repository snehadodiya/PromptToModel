 # Remove rows with missing values
df = df.dropna()

# Convert 'Manufacture Date' column to datetime format
df['Manufacture Date'] = pd.to_datetime(df['Manufacture Date'])

# Create a new column for age of the car
df['Age'] = (pd.DateTimeIndex.today() - df['Manufacture Date']).dt.days // 365

# Remove 'Manufacture Date' column as it's no longer needed
df = df.drop(columns=['Manufacture Date'])

# Convert 'Price' column to numeric type
df['Price'] = pd.to_numeric(df['Price'])

# Replace any non-numerical values in 'Kms Driven' column with NaN
df['Kms Driven'] = df['Kms Driven'].apply(lambda x: np.nan if not all(c.isdigit() for c in x) else x)
df['Kms Driven'] = pd.to_numeric(df['Kms Driven'], errors='coerce')

# Remove 'Car Name' column as it's not relevant for numerical analysis
df = df.drop(columns=['Car Name'])

# Save the cleaned dataframe to a file
df.to_csv("output_step_cleaned_data.csv", index=False)

with open("output_step_cleaning_summary.txt", "w") as f:
    f.write("Cleaning Summary:\n")
    f.write("- Removed rows with missing values\n")
    f.write("- Converted 'Manufacture Date' to datetime format\n")
    f.write("- Calculated car age and removed 'Manufacture Date' column\n")
    f.write("- Converted 'Price' to numeric type\n")
    f.write("- Replaced non-numeric values in 'Kms Driven' with NaN and converted to numeric type\n")
    f.write("- Removed 'Car Name' column")

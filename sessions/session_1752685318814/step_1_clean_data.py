 # Remove rows with missing values
df = df.dropna()

# Convert 'Manufacture Date' column to datetime format
df['Manufacture Date'] = pd.to_datetime(df['Manufacture Date'])

# Create a new column 'Age' to store the age of the car based on the manufacturing date
df['Age'] = (pd.Timestamp('now') - df['Manufacture Date']).dt.days // 365

# Remove the 'Manufacture Date' column as it's not needed anymore
df = df.drop(columns=['Manufacture Date'])

# Convert 'Price' column to numeric type
df['Price'] = pd.to_numeric(df['Price'])

# Replace 'Kms Driven' values greater than 500,000 with the mean of the rest of the data
mean_kms = df['Kms Driven'][df['Kms Driven'] < 500000].mean()
df.loc[df['Kms Driven'] > 500000, 'Kms Driven'] = mean_kms

# Save the cleaned dataframe as a parquet file
df.to_parquet("cleaned_df.parquet")

with open("output_step_clean_data.txt", "w") as f:
    f.write("Cleaned data saved as 'cleaned_df.parquet'\n")
    f.write(f"Number of rows before cleaning: {len(df.loc[df['Price'].isna()])}\n")
    f.write(f"Number of rows after cleaning: {len(df)}\n")

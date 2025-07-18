 # Remove rows with missing values
df = df.dropna()

# Convert 'Manufacture Date' column to datetime format
df['Manufacture Date'] = pd.to_datetime(df['Manufacture Date'])

# Create a new column 'Age' by calculating the difference between current date and 'Manufacture Date'
current_date = pd.Timestamp('now')
df['Age'] = (current_date - df['Manufacture Date']).dt.days / 365

# Save the cleaned data to a text file
with open("output_step_1.txt", "w") as f:
    f.write(df.to_string())

# Save the cleaned data as a CSV file
df.to_csv("cleaned_data.csv", index=False)

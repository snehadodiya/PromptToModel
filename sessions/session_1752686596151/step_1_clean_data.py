 # Remove rows with missing values
df = df.dropna()

# Convert 'Manufacture Date' column to datetime
df['Manufacture Date'] = pd.to_datetime(df['Manufacture Date'])

# Create a new column 'Age' by subtracting the manufacture date from today
today = pd.Timestamp('now')
df['Age'] = (today - df['Manufacture Date']).dt.days // 365

# Remove the 'Manufacture Date' column as it's no longer needed
df = df.drop('Manufacture Date', axis=1)

# Replace spaces in 'Car Name' with underscores
df['Car Name'] = df['Car Name'].str.replace(' ', '_')

# Convert 'Price' column to numeric
df['Price'] = pd.to_numeric(df['Price'])

# Convert 'Kms Driven' column to numeric
df['Kms Driven'] = pd.to_numeric(df['Kms Driven'])

# Replace 'kilometers' with 'k' in 'Kms Driven' column
df['Kms Driven'] = df['Kms Driven'].str.replace('kilometers', 'k')

# Replace fuel types with their initials
fuel_dict = {'Petrol': 'P', 'Diesel': 'D', 'Electric': 'E'}
df['Fuel Type'] = df['Fuel Type'].map(fuel_dict)

# Replace transmission types with their initials
transmission_dict = {'Manual': 'M', 'Automatic': 'A'}
df['Transmission'] = df['Transmission'].map(transmission_dict)

# Replace ownership types with their initials
ownership_dict = {'First Owner': '1', 'Second Owner': '2', 'Third Owner': '3', 'Fourth Owner': '4', 'Fifth Owner': '5'}
df['Ownership'] = df['Ownership'].map(ownership_dict)

# Save the cleaned dataframe to a file
with open("output_step_1.txt", "w") as f:
    f.write(df.to_string())

# Save a histogram of car ages
plt.hist(df['Age'], bins=20)
plt.savefig("output_step_1.png")

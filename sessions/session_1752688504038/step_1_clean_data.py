 # Step 0: Remove rows with missing values
df.dropna(inplace=True)

# Step 1: Convert 'Manufacture Date' column to datetime
df['Manufacture Date'] = pd.to_datetime(df['Manufacture Date'])

# Step 2: Extract year from 'Manufacture Date'
df['Manufacture Year'] = df['Manufacture Date'].dt.year
df.drop('Manufacture Date', axis=1, inplace=True)

# Step 3: Convert 'Price' and 'Kms Driven' to float
df[['Price', 'Kms Driven']] = df[['Price', 'Kms Driven']].astype(float)

# Step 4: Replace ' years' with '' in 'Manufacturer' column
df['Manufacturer'] = df['Manufacturer'].str.replace(' years', '', regex=True)

# Step 5: Replace ' - ' with ' ' in 'Manufacturer' column
df['Manufacturer'] = df['Manufacturer'].str.replace(' - ', ' ', regex=True)

# Step 6: Convert 'Manufacturer' to lowercase
df['Manufacturer'] = df['Manufacturer'].str.lower()

# Step 7: Replace ' petrol' with 'Petrol' in 'Fuel Type' column
df['Fuel Type'] = df['Fuel Type'].str.replace(' petrol', 'Petrol', regex=True)

# Step 8: Replace ' diesel' with 'Diesel' in 'Fuel Type' column
df['Fuel Type'] = df['Fuel Type'].str.replace(' diesel', 'Diesel', regex=True)

# Step 9: Replace ' automatic' with 'Automatic' in 'Transmission' column
df['Transmission'] = df['Transmission'].str.replace(' automatic', 'Automatic', regex=True)

# Step 10: Replace ' manual' with 'Manual' in 'Transmission' column
df['Transmission'] = df['Transmission'].str.replace(' manual', 'Manual', regex=True)

# Step 11: Replace ' ownership' with 'First Owner' in 'Ownership' column
df['Ownership'] = df['Ownership'].str.replace(' ownership', 'First Owner', regex=True)

# Step 12: Replace '(used)' with '' in 'Car Name' column
df['Car Name'] = df['Car Name'].str.replace('\(used\)', '', regex=True)

with open("output_step_clean_data.txt", "w") as f:
    f.write(str(df.head()))
plt.savefig("output_step_clean_data.png")

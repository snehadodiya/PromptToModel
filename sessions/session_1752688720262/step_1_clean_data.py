 # Step 1: Remove rows with missing values
df = df.dropna()

# Step 2: Convert 'Manufacture Date' column to datetime format
df['Manufacture Date'] = pd.to_datetime(df['Manufacture Date'])

# Step 3: Create a function to clean 'Price' column
def clean_price(price):
    try:
        price = float(price.replace(',', '').replace(' lakhs', '').replace(' lakh', ''))
        return price
    except:
        return None

# Step 4: Apply the function to 'Price' column and drop rows with missing values
df['Price'] = df['Price'].apply(clean_price)
df = df.dropna(subset=['Price'])

# Step 5: Convert 'Kms Driven' to float type
df['Kms Driven'] = df['Kms Driven'].astype(float)

# Step 6: Convert 'Seats' to integer type
df['Seats'] = df['Seats'].astype(int)

# Save cleaned data to a file
df.to_csv("cleaned_data.csv", index=False)

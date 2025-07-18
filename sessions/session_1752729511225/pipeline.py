import pandas as pd

import matplotlib.pyplot as plt

df = pd.read_csv('dataset.csv')


# ---- step_1_clean_data.py ----
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("dataset.csv")

 # Remove rows with missing values
df = df.dropna()

# Convert 'Manufacture Date' column to datetime format
df['Manufacture Date'] = pd.to_datetime(df['Manufacture Date'])

# Create a new column 'Age' by subtracting the manufacture date from today
todays_date = pd.Timestamp('2022-04-12')
df['Age'] = (todays_date - df['Manufacture Date']).dt.days

# Convert 'Price' column to numeric type
df['Price'] = pd.to_numeric(df['Price'])

# Replace any non-numeric values in 'Kms Driven' with NaN and then drop rows with NaN values
df['Kms Driven'] = pd.to_numeric(df['Kms Driven'], errors='coerce')
df = df.dropna(subset=['Kms Driven'])

# Replace 'Yes' and 'No' values in 'Transmission' column with 'Manual' and 'Automatic' respectively
df['Transmission'] = df['Transmission'].replace({'Yes': 'Manual', 'No': 'Automatic'})

# Replace 'Yes' and 'No' values in 'Ownership' column with 'First' and 'Second' respectively
df['Ownership'] = df['Ownership'].replace({'Yes': 'First', 'No': 'Second'})

# Save cleaned data to a file
df.to_csv("cleaned_data.csv", index=False)

with open("output_step_1.txt", "w") as f:
    f.write("Cleaned data saved to 'cleaned_data.csv'\n")
    f.write(df.head().to_string())



# ---- step_2_create_ridge_model.py ----
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("dataset.csv")

 from sklearn.linear_model import Ridge
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures

# Define features and target
X = df.drop(['Car Name', 'Price'], axis=1)
y = df['Price']

# Create polynomial and interaction features
poly = PolynomialFeatures(degree=2, interaction_only=False, include_bias=False)
X_poly = poly.fit_transform(X)

# Split data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X_poly, y, test_size=0.3, random_state=42)

# Create and fit Ridge model
ridge = Ridge(alpha=1.0)
ridge.fit(X_train, y_train)

# Save the plot
plt.savefig("output_step_1.png")

# Save the model summary
with open("output_step_1.txt", "w") as f:
    f.write(str(ridge.intercept_) + "\n")
    f.write(str(ridge.coef_) + "\n")
    f.write(str(ridge.score(X_test, y_test)) + "\n")

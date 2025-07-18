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
today = pd.Timestamp('now')
df['Age'] = today.year - df['Manufacture Date'].dt.year - ((today.month, today.day) < ('Manufacture Date'.dt.month, 'Manufacture Date'.dt.day))

# Remove 'Manufacture Date' column
df = df.drop(columns=['Manufacture Date'])

# Convert 'Price' and 'Kms Driven' columns to numeric types
df[['Price', 'Kms Driven']] = df[['Price', 'Kms Driven']].apply(pd.to_numeric)

# Replace 'Unknown' values in 'Fuel Type' column with 'Petrol'
df['Fuel Type'] = df['Fuel Type'].replace('Unknown', 'Petrol')

# Replace 'Unknown' values in 'Transmission' column with 'Manual'
df['Transmission'] = df['Transmission'].replace('Unknown', 'Manual')

# Replace 'NaN' values in 'Ownership' column with 'First Owner'
df['Ownership'] = df['Ownership'].replace('NaN', 'First Owner')

# Save the cleaned DataFrame as a CSV file
df.to_csv("cleaned_data.csv", index=False)

with open("output_step_1.txt", "w") as f:
    f.write("Cleaned data saved to 'cleaned_data.csv'")



# ---- step_2_remove_transmission_column.py ----
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("dataset.csv")

 ```python
df = df.drop('Transmission', axis=1)
```



# ---- step_3_train_this_dataset.py ----
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("dataset.csv")

 From the provided dataset, let's assume that we want to predict the 'Price' based on other features. Here's how you can create a machine learning model using Scikit-learn:

```python
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Ensure there are no missing values
df = df.dropna()

# Create features and target arrays
X = df.drop('Price', axis=1)
y = df['Price']

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Save the coefficients and intercept to a text file
with open("output_step_1.txt", "w") as f:
    f.write("Intercept: {:.2f}\n".format(model.intercept_))
    for i, v in enumerate(model.coef_):
        f.write("Coefficient for feature {}: {:.2f}\n".format(X.columns[i], v))

# Save the plot of feature importances
import matplotlib.pyplot as plt

coef = pd.Series(model.coef_, index=X.columns)
coef.plot(kind='bar')
plt.savefig("output_step_2.png")

# Evaluate the model
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# Save the evaluation results to a text file
with open("output_step_3.txt", "w") as f:
    f.write("Mean Squared Error: {:.2f}\n".format(mse))
    f.write("R-squared: {:.2f}".format(r2))
```

This code will create a linear regression model, save the coefficients and intercept to a text file, plot feature importances, and evaluate the model using mean squared error and R-squared metrics.

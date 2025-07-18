import pandas as pd

import matplotlib.pyplot as plt

df = pd.read_csv('dataset.csv')


# ---- step_1_clean_this_data.py ----
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("dataset.csv")

 ```python
# Replace any null or NaN values in the DataFrame with the mean of the column
df = df.fillna(df.mean())

# Convert the 'Manufacture Date' column to datetime format
df['Manufacture Date'] = pd.to_datetime(df['Manufacture Date'])

# Create a new column 'Age' by subtracting the 'Manufacture Date' from the current date
df['Age'] = (pd.to_datetime('2022-04-01') - df['Manufacture Date']).dt.days // 365

# Remove the 'Manufacture Date' column as it's no longer needed
df = df.drop(columns=['Manufacture Date'])

# Save the cleaned DataFrame to a text file
with open("output_step_1.txt", "w") as f:
    f.write(df.to_string())
```



# ---- step_2_remove_missing_entries.py ----
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("dataset.csv")

 ```python
df = df.dropna()
```
The provided code removes any rows with missing values from the DataFrame 'df'.



# ---- step_3_create_a_model.py ----
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("dataset.csv")

 From sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LinearRegression

label_encoder = LabelEncoder()
df['Manufacturer'] = label_encoder.fit_transform(df['Manufacturer'])
df['Fuel Type'] = label_encoder.fit_transform(df['Fuel Type'])
df['Transmission'] = label_encoder.fit_transform(df['Transmission'])

X = df.drop('Price', axis=1)
y = df['Price']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

with open("output_step_1.txt", "w") as f:
    f.write("Model coefficients:\n" + str(model.coef_))
    f.write("\nIntercept: " + str(model.intercept_))

plt.scatter(y_test, model.predict(X_test))
plt.savefig("output_step_1.png")

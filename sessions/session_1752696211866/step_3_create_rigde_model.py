import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("dataset.csv")

from sklearn.linear_model import Ridge
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
import pandas as pd
import numpy as np

# Preprocessing
df = df.drop(columns=['Car Name'])
df['Manufacture Date'] = pd.to_datetime(df['Manufacture Date'])
df['Manufacture Year'] = df['Manufacture Date'].dt.year
df = df.drop(columns=['Manufacture Date'])

label_encoder = LabelEncoder()
df['Fuel Type'] = label_encoder.fit_transform(df['Fuel Type'])
df['Transmission'] = label_encoder.fit_transform(df['Transmission'])
df['Ownership'] = label_encoder.fit_transform(df['Ownership'])
df['Manufacturer'] = label_encoder.fit_transform(df['Manufacturer'])

onehot_encoder = OneHotEncoder(sparse=False)
df = pd.DataFrame(onehot_encoder.fit_transform(df[['Manufacturer']]), columns=onehot_encoder.categories_[0])
df = df.drop(columns=['Manufacturer'])

X = df.drop(columns=['Price'])
y = df['Price']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Ridge Regression
ridge = Ridge(alpha=1.0)
ridge.fit(X_train, y_train)

# Save the coefficients
with open("output_step_1.txt", "w") as f:
    f.write("Ridge Coefficients:\n")
    f.write(str(ridge.coef_))

# Save the plot
plt.plot(ridge.alphas_, ridge.scorer_(X_train, y_train), label="Training Score")
plt.plot(ridge.alphas_, ridge.scorer_(X_test, y_test), label="Test Score")
plt.legend()
plt.savefig("output_step_2.png")

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

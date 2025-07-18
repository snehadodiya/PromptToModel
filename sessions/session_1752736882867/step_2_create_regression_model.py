import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("dataset.csv")

 # Create a regression model using Linear Regression
from sklearn.linear_model import LinearRegression

# Assume 'Price' is the target variable and the rest are features
X = df.drop('Price', axis=1)
y = df['Price']

model = LinearRegression()
model.fit(X, y)

# Print the R^2 score for evaluation
with open("output_step_1.txt", "w") as f:
    f.write(f"R^2 score: {model.score(X, y):.2f}")

# Save the plot of residuals
model.predict(X).head().plot(kind='scatter', label='Predicted Prices')
y.plot(label='Actual Prices', figsize=(10, 5))
plt.legend()
plt.savefig("output_step_2.png")

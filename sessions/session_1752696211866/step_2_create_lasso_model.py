import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("dataset.csv")

 from sklearn.linear_model import Lasso
from sklearn.model_selection import train_test_split

X = df.drop('Price', axis=1)
y = df['Price']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = Lasso(alpha=0.1)
model.fit(X_train, y_train)

with open("output_step_1.txt", "w") as f:
    f.write(f"Lasso coefficients:\n{model.coef_}\n")

plt.scatter(y_test, model.predict(X_test))
plt.savefig("output_step_2.png")

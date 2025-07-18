import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("dataset.csv")

 From sklearn.ensemble import RandomForestRegressor

model = RandomForestRegressor(n_estimators=100, random_state=0)

# Since the user didn't specify which column to predict,
# let's assume we want to predict the 'Price' based on other features.
X = df.drop('Price', axis=1)
y = df['Price']

with open("output_step_1.txt", "w") as f:
    f.write("Model created: Random Forest Regressor with 100 trees.\n"
            "Predicting 'Price' based on other features.\n"
            f"Number of samples: {len(df)}\n"
            f"Number of features: {X.shape[1]}")

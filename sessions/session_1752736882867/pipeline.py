import pandas as pd

import matplotlib.pyplot as plt

df = pd.read_csv('dataset.csv')


# ---- step_1_remove_seats_column.py ----
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("dataset.csv")

 ```python
df = df.drop('Seats', axis=1)
df = df.dropna()

with open("output_step_1.txt", "w") as f:
    f.write("Seats column removed and missing entries dropped.")
plt.savefig("output_step_1.png")  # no need to create an empty plot, so saving it empty
```



# ---- step_2_create_regression_model.py ----
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



# ---- step_3_show_me_first.py ----
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("dataset.csv")

 with open("output_step_1.txt", "w") as f:
    f.write(df.head(20).to_string())

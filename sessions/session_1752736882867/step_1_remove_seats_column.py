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

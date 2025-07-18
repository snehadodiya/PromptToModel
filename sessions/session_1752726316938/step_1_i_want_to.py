import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("dataset.csv")

 ```python
# Remove transmission column
df = df.drop('Transmission', axis=1)

# Remove rows with missing entries
df = df.dropna()

# Save a summary of the DataFrame to a text file
with open("output_step_1.txt", "w") as f:
    f.write(df.head().to_string())
```

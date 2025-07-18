import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("dataset.csv")

 ```python
df = df.dropna()
```
The provided code removes any rows with missing values from the DataFrame 'df'.

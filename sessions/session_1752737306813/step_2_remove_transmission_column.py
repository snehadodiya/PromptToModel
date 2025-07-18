import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("dataset.csv")

 ```python
df = df.drop('Transmission', axis=1)
```

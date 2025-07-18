import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("dataset.csv")

 with open("output_step_1.txt", "w") as f:
    f.write(df.head(20).to_string())

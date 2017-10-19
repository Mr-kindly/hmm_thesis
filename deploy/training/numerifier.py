import numpy as np
import pandas as pd

df = pd.read_csv('AGI.csv')
# print df
x = df["Open"]
print df["Open"]

data = x.reindex(index = x.index[::-1])
g = data.as_matrix()
print g
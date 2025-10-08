import pandas as pd

data = pd.read_csv("data (1).csv")

rows = pd.DataFrame(data, index= [0, 1, 2, 3, 4])

print(data)
print(data.info())
print(data.describe())

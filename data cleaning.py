import pandas as pd
import matplotlib as plt

data = pd.read_csv('data (1).csv')
new_data = data.dropna()

data.plot(kind= "scatter", x = "Maxpulse", y= "Duration")

plt.show()
import pandas as pd

data = pd.read_csv('data (1).csv')
sorted_data = data.sort_values(by="Pulse")
sum_pulse = data["Pulse"].sum()
max_pulse = data["Pulse"].max()
mean_pulse = data["Pulse"].mean()

print(f"""The sum is {sum_pulse}
the max pulse is {max_pulse}
the mean of the pulses are {mean_pulse}
the list sorted by pulses is:
{sorted_data}""")
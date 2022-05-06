import pandas as pd

import matplotlib.pyplot as plt

Nasdaq = pd.read_csv("Nasdaq.csv")
Nasdaq["Date"] = pd.to_datetime(Nasdaq["Date"])
print(Nasdaq.head())
dati=Nasdaq.loc[Nasdaq["Date"]>"1985-00-00"]
plt.plot(Nasdaq.Date, Nasdaq.Volume)

plt.show()

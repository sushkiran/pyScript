"""
You are given a dataset, containing the number of hurricanes occurring in the United States
along the coast of the Atlantic. Load the data from the dataset into your program and plot a
Bar Graph of the data, taking the Year as the x-axis and the number of hurricanes occurring as
the Y-axis.
"""

import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('Hurricanes.csv')
plt.bar(pd.Series(df.Year), pd.Series(df.Hurricanes))
plt.show()
plt.close()



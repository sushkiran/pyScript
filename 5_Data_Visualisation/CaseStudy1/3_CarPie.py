"""
Plot a pie-chart of the number of models released by every manufacturer, recorded in the data provide.
Also mention the name of the manufacture with the largest releases.
"""

import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('Cars2015.csv')
df['Make'] = df['Make'].str.strip()
new_df = df.groupby('Make')['Model'].count().reset_index()
print(new_df.max())

plt.figure(figsize=(8,7))
plt.pie(new_df['Model'], labels=new_df['Make'])
plt.show()
plt.close()
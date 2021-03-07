"""
The dataset given, records data of city temperatures over the years 2014 and 2015.
Plot the histogram of the temperatures over this period for the cities of San Francisco and Moscow
"""

import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('CityTemps.csv')

fig, ax = plt.subplots(2, 2)
fig.tight_layout(h_pad=2)

plt.subplot(2, 2, 1)
plt.hist(df[df['Year']==2014]['Moscow'], bins=5)
plt.title('Moscow 2014')

plt.subplot(2, 2, 2)
plt.hist(df[df['Year']==2014]['San Francisco'], bins=5)
plt.title('San Francisco 2014')

plt.subplot(2, 2, 3)
plt.hist(df[df['Year']==2015]['Moscow'], bins=5)
plt.title('Moscow 2015')

plt.subplot(2, 2, 4)
plt.hist(df[df['Year']==2015]['San Francisco'], bins=5)
plt.title('San Francisco 2015')

plt.subplots_adjust(top=0.85)
plt.suptitle('City Temperatures')
plt.show()
plt.close()

"""
5.8: Draw a scatter graph of any 50 random values of x and y axis
5.9: Create a dataframe from following data
    'first_name': ['Jason', 'Molly', 'Tina', 'Jake', 'Amy'],
    'last_name': ['Miller', 'Jacobson', 'Ali', 'Milner', 'Cooze'],
    'female': [0, 1, 1, 0, 1],
    'age': [42, 52, 36, 24, 73],
    'preTestScore': [4, 24, 31, 2, 3],
    'postTestScore': [25, 94, 57, 62, 70]
    Draw a Scatter plot of preTestScore and postTestScore, with the size of each point determined by age
5.10: Draw a Scatter plot from the data in question 9 of preTestScore and postTestScore with the size = 300
    and the color determined by sex
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

fig, ax = plt.subplots(1, 3, figsize=(10, 5), dpi=100)
fig.tight_layout(h_pad=2)

x = range(50)
y = range(50) + np.random.randint(0,30,50)

# 5.8: Draw a scatter graph of any 50 random values of x and y axis
plt.subplot(1, 3, 1)
plt.scatter(x, y)
plt.title('Random Scatter')

# 5.9: Create a dataframe from following data
data = {
    'first_name': ['Jason', 'Molly', 'Tina', 'Jake', 'Amy'],
    'last_name': ['Miller', 'Jacobson', 'Ali', 'Milner', 'Cooze'],
    'female': [0, 1, 1, 0, 1],
    'age': [42, 52, 36, 24, 73],
    'preTestScore': [4, 24, 31, 2, 3],
    'postTestScore': [25, 94, 57, 62, 70]
}
df = pd.DataFrame(data)

# 5.9: Draw a Scatter plot of preTestScore and postTestScore, with the size of each point determined by age
plt.subplot(1, 3, 2)
plt.scatter(df['preTestScore'], df['postTestScore'], s=df['age'])
plt.title('Test Score Scatter by age')


# 5.10: Draw a Scatter plot of preTestScore and postTestScore with the size = 300 and the color determined by sex
plt.subplot(1, 3, 3)
plt.scatter(df['preTestScore'], df['postTestScore'], s=300, c=df['female'])
plt.title('Test Score Scatter by Sex')

plt.subplots_adjust(top=0.85, bottom=0.1, left=0.08)
plt.suptitle('Scatter Plot Example', fontsize=14)

plt.show()
plt.close()

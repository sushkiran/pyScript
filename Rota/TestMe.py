import numpy as np
import pandas as pd

arr = np.asarray(['Naveen', 'Sushvin', 'Divik', 'Kapil'])
#not_me = ['Kapil','Sushvin']
not_me = 'Divik'

mask = []
for element in arr:
    mask.append(element not in not_me)

print(list(arr[mask]))





'''
groups={
    'A': ['Divik'],
    'B': ['Kapil','Sushvin'],
    'C': ['Naveen']
}
print(groups['B'])
'''
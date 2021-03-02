import numpy as np

#a = [['Naveen'], ['Kapil', 'Sushvin']]
a = ['Naveen']
'''b = np.array(a,dtype=object)
c = b.reshape(-1)
print(c)
print(list(c))'''

print(len(a))

f = []
for x in a:
    for y in x:
        f.append(y)
print(f)

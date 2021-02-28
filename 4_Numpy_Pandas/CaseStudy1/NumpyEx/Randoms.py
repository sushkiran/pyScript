import numpy as np
from numpy import random

"""
8. Create a 10x10 array with random values and find the minimum and maximum values.
"""

print('\n--- Question 8 ---')
eight = random.rand(10, 10)
print(eight)
print('Minimum:', eight.min(), "Maximum:", eight.max())

"""
9. Create a random vector of size 30 and find the mean value.
"""

print('\n--- Question 9 ---')
nine = random.rand(30)
print(nine)
print('Mean value:', nine.mean())

"""
11. Create a random array of 3 rows and 3 columns and sort it according to 1st column, 2nd column or 3rd column.
"""
print('\n--- Question 11 ---')
eleven = random.rand(3, 3)
print(eleven)

print('\nSorted on 1st column:')
print(np.sort(eleven, axis=0))

"""
12. Create a four dimensions array get sum over the last two axis at once.
"""
print('\n--- Question 12 ---')
twelve = random.randint(10, size=(3, 2, 3, 4))
print(twelve)

print('\nSum on Last two axis at once:')
print(twelve.sum(axis=(-1, -2)))
"""
13. Create a random array and swap two rows of an array.
"""
print('\n--- Question 13 ---')
thirteen = random.randint(10, size=(6,3))
print(thirteen)

thirteen[[2, 4]] = thirteen[[4, 2]]
print('\n After Swapping the 2nd and 4th row')
print(thirteen)

"""
14. Create a random matrix and Compute a matrix rank.
"""

print('\n--- Question 14 ---')
fourteen = random.randint(20, size=(4, 3))
print(fourteen)
print('\nMatrix rank:', np.linalg.matrix_rank(fourteen))

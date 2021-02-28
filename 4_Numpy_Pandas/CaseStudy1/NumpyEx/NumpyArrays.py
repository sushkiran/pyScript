import numpy as np

"""
5. How do you Count The Number Of Times Each Value Appears In An Array Of Integers?
[0, 5, 4, 0, 4, 4, 3, 0, 0, 5, 2, 1, 1, 9]
Answer should be array([4, 2, 1, 1, 3, 2, 0, 0, 0, 1]) which means
0 comes 4 times, 1 comes 2 times, 2 comes 1 time, 3 comes 1 time and so on.
"""
print('\n--- Question 5 ---')

a_five = np.array([0, 5, 4, 0, 4, 4, 3, 0, 0, 5, 2, 1, 1, 9])
text = 'Number {} comes {} times'
for i in range(10):
    a5_cond = (a_five == i)
    x = len(a_five[a5_cond])
    if x > 0:
        print(text.format(i, x))

"""
6. Create a numpy array [[0, 1, 2], [ 3, 4, 5], [ 6, 7, 8],[ 9, 10, 11]]) and filter the elements greater than 5.
"""
print('\n--- Question 6 ---')

a_six = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]])
print(a_six)

a6_cond = (a_six > 5)
print(a_six[a6_cond])

"""
7. Create a numpy array having NaN (Not a Number) and print it.
array([ nan, 1., 2., nan, 3., 4., 5.])
Print the same array omitting all elements which are nan
"""

print('\n--- Question 7 ---')

a_seven = np.array([np.nan, 1., 2., np.nan, 3., 4., 5.])
print(a_seven)
print(a_seven[~np.isnan(a_seven)])

"""
10. Create numpy array having elements 0 to 10 And negate all the elements between 3 and 9
"""

print('\n--- Question 10 ---')

a_ten = np.array(range(11))
print(a_ten)

a_ten = np.array(list(map(lambda num: num * -1 if 3 <= num <= 9 else num, a_ten)))
print(a_ten)

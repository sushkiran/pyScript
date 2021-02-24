from functools import reduce

'''
items = [1, 2, 3, 4, 5]
print(list(map(lambda x: x**2, items)))
print(reduce(lambda x, y: x * y, items))
print(reduce(lambda x, y: x**2 * y**2, items))


string = '630'
print(string[:-2])
print(string[-2:])

string = '1630'
print(string[:-2])
print(string[-2:])


i =10
x = str(i)
print(i)
print(x[0])
'''

n = int(input('Enter: '))
print(reduce(lambda x, y: x * y, range(1, n + 1)))

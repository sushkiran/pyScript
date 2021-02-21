from functools import reduce

items = [1, 2, 3, 4, 5]
print(list(map(lambda x: x**2, items)))
print(reduce(lambda x, y: x * y, items))
print(reduce(lambda x, y: x**2 * y**2, items))

import random

# 1. Output of below is 4
nums = set([1, 1, 2, 3, 3, 3, 4, 4])
print('Q01=', len(nums))

# 2. Output of below is ['john', 'peter']
d = {"john": 40, "peter": 45}
print('Q02=', list(d.keys()))

# 4.Write a for loop that prints all elements of a list and their position in the list.
a = [4, 7, 3, 2, 5, 9]
for i in a:
    print('Q04=', 'element', i, 'is at position#', a.index(i))

# 8. Write a program to make a list whose elements are intersection of given lists
list1 = [1, 3, 6, 78, 35, 55]
list2 = [12, 24, 35, 24, 88, 120, 155]
print('Q08= intersection of both', list(set(list1).intersection(list2)))

# 9. Write a program to remove all duplicate values from the given list with original order reserved
list3 = [12, 24, 35, 24, 88, 120, 155, 88, 120, 155]
print('Q09=',sorted(set(list3), reverse=True))

# 10. By using list comprehension, please write a program to print the list after removing the value 24
listComp = [12, 24, 35, 24, 88, 120, 155]
list4 = [x for x in listComp if x != 24]
print('Q10=', list4)

# 11. By using list comprehension, please write a program to print the list after removing the 0th,4th,5th numbers
list5 = [x for x in listComp if listComp.index(x) not in (0, 4, 5)]
print('Q11=', list5)

# 12. By using list comprehension, please write a program to print the list after removing numbers divisible by 5 & 7
list6 = [x for x in listComp if 0 not in (x % 5, x % 7)]
print('Q12=', list6)

# 13. Please write a program to randomly generate a list with 5 numbers, which are divisible by 5 and 7,
# between 1 and 1000 inclusive
result = []
for x in range(1, 1001):
    if x % 5 == 0 and x % 7 == 0:
        result.append(x)
print('Q13=', random.sample(result, 5))

# 14. Write a program to compute  1/2+2/3+3/4+...+n/n+1 with a given n input by console (n>0)
n = 5
out = 0
for i in range(1, n+1):
    out += i/(i+1)
print('Q14=', out)
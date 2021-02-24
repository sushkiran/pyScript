import math
from functools import reduce


'''
Q6. Write a program which will find all such numbers which are divisible by 7 
but are not a multiple of 5, between 2000 and 3200 (both included). 
The numbers obtained should be printed in a comma-separated sequence on a single line.
'''


def q6_divisible():
    data = list(filter(lambda x: x % 7 == 0 and x % 5 != 0, range(2000, 3200)))
    print(data)


'''
Q7. Write a program which can compute the factorial of a given numbers. Use recursion to find it.
Hint: Suppose the following input is supplied to the program: 8
Then, the output should be: 40320
'''


def recur_factorial(number):
    if number == 1:
        return number
    else:
        return number * recur_factorial(number - 1)


def q7_factorial():
    num = int(input("Enter a number: "))
    if num < 0:
        print("Sorry, factorial does not exist for negative numbers")
    elif num == 0:
        print("The factorial of 0 is 1")
    else:
        r_fact = recur_factorial(num)
        l_fact = reduce(lambda x, y: x * y, range(1, num + 1))
        text = 'Factorial of {} is {} using recursion and {} using Lambda reduce'
        print(text.format(num, r_fact, l_fact))


'''
Q8. Write a program that calculates and prints the value according to the given formula:
Q = Square root of [(2 * C * D)/H]
Following are the fixed values of C and H: C is 50. H is 30.
D is the variable whose values should be input to your program in a comma- separated sequence.
Example:
Let us assume the following comma separated input sequence is given to the program:
100,150,180
The output of the program should be:
18,22,24
'''


def q8_lambda():
    items = [100, 150, 180]
    c = 50
    h = 30
    print(list(map(lambda d: int(math.sqrt((2 * c * int(d)) / h)), items)))


if __name__ == '__main__':
    # q6_divisible()
    # q7_factorial()
    q8_lambda()




from functools import reduce


'''
Q2. Data of XYZ company is stored in sorted list. Write a program for searching
specific data from that list.
Hint: Use if/elif to deal with conditions.
'''


def q2_xyz_sorted():
    data = ['a1', 'a2', 'a3', 'a4', 'a5']
    to_search = 'a4'
    if to_search in data:
        print('found', to_search)
    else:
        print(to_search, 'cannot be found')


'''
Q6. Write a program which will find all such numbers which are divisible by 7 
but are not a multiple of 5, between 2000 and 3200 (both included). 
The numbers obtained should be printed in a comma-separated sequence on a single line.
'''


def q6_divisible():
    data = []
    for number in range(2000, 3200):
        if number % 7 == 0 and number % 5 != 0:
            data.append(number)
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
    # take input from the user


def q7_factorial():
    num = int(input("Enter a number: "))
    # check is the number is negative
    if num < 0:
        print("Sorry, factorial does not exist for negative numbers")
    elif num == 0:
        print("The factorial of 0 is 1")
    else:
        r_fact = recur_factorial(num)
        l_fact = reduce(lambda x, y: x * y, range(1, num + 1))
        text = 'Factorial of {} is {} using recursion and {} using Lambda reduce'
        print(text.format(num, r_fact, l_fact))



if __name__ == '__main__':
    # q2_xyz_sorted()
    # q6_divisible()
    q7_factorial()

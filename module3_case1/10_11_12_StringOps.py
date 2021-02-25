'''
Q10. Write a program that accepts a comma separated sequence of words as input
and prints the words in a comma-separated sequence after sorting them alphabetically.
Suppose the following input is supplied to the program:
without,hello,bag,world
Then,the output should be:
bag,hello,without,world
'''


def q10_sort_input():
    input_str = input('Enter strings to sort (comma separated): ')
    print('The sorted output is:', sorted(input_str.split(',')))


'''
Q11. Write a program that accepts sequence of lines as input 
and prints the lines after making all characters in the sentence capitalized.
Suppose the following input is supplied to the program:
Hello world, Practice makes perfect
Then, the output should be:
HELLO WORLD, PRACTICE MAKES PERFECT
'''


def q11_capitalize_input():
    input_str = input('Enter string to capitalize: ')
    print(input_str.upper())


'''
Q12. Write a program that accepts a sequence of whitespace separated words as input 
and prints the words after removing all duplicate words and sorting them alphanumerically.
Suppose the following input is supplied to the program:
hello world and practice makes perfect and hello world again
Then, the output should be:
again and hello makes perfect practice world
'''


def q12_sort_input():
    input_str = input('Enter strings to sort (comma separated): ')
    print('The sorted output is:', sorted(set(input_str.split(' '))))


'''
All combined: Q10 + Q11 + Q12. Use below sample to test:
hello,world,and,practice,makes,perfect,and,hello,world,again
'''


def all_combined():
    input_str = input('Enter string (comma separated): ')
    q10_data = input_str
    q11_data = input_str
    q12_data = input_str
    print('Q10. Sorted List :', sorted(q10_data.split(',')))
    print('Q11. Capitalized :', q11_data.upper())
    print('Q12. Sorted Set  :', sorted(set(q12_data.split(','))))


if __name__ == '__main__':
    # q10_sort_input()
    # q11_capitalize_input()
    # q12_sort_input()
    all_combined()

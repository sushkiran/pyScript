"""
14. Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
Suppose the following input is supplied to the program:
Hello world!
Then, the output should be:
UPPER CASE 1
LOWER CASE 9
"""


input_str = input("Enter string: ")

print('Uppercase count:', len(list(filter(lambda x: x.isupper() is True, input_str))))
print('Lowercase count:', len(list(filter(lambda x: x.islower() is True, input_str))))


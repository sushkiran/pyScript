'''
Q13. Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input
and then check whether they are divisible by 5 or not.
The numbers that are divisible by 5 are to be printed in a comma separated sequence.
Example: 0100,0011,1010,1001
Then the output should be: 1010
'''

# 0001,0010,0011,0100,0101,0110,0111,1111
input_str = input('Enter list of binary numbers: ')

# split the string and convert each item to integer, saved as a list of numbers.
input_list_int = list(map(lambda x: int(x), input_str.split(',')))

# select only those that are divisible by 5
div_5_list = list(filter(lambda x: x % 5 == 0, input_list_int))

# convert each item back to String and re-pad missing zeroes, saved as a list of strings
out_list_str = list(map(lambda x: str(x).zfill(4), div_5_list))

print(','.join(out_list_str))


'''
A website requires a user to input username and password to register.
Write a program to check the validity of password given by user.
Following are the criteria for checking password:
1. At least 1 letter between [a-z]
2. At least 1 number between [0-9]
3. At least 1 letter between [A-Z]
4. At least 1 character from [$#@]
5. Minimum length of transaction password: 6
6. Maximum length of transaction password: 12
'''


def isValid(pwd):
    if 6 <= len(pwd) <= 12:
        digit = 0
        upper = 0
        lower = 0
        special = 0
        for i in pwd:
            if i.isupper():
                upper += 1
            elif i.islower():
                lower += 1
            elif i.isdigit():
                digit += 1
            else:
                special += 1

        if 0 in (digit, upper, lower, special):
            return 'Password is NOT Valid'
        else:
            return 'Password is Valid'
    return 'Password is NOT Valid'


print(isValid(input('Enter password:')))


# 5.Please write a program which accepts a string from console and print the characters that have even indexes
string = input('Q5= Enter Alphanumeric String:')
inList = list(string)
outList = []
for i in inList:
    if inList.index(i) % 2 != 0:
        outList.append(i)
print(''.join(outList))

# 6. Please write a program which accepts a string from console and print it in reverse order
string = input('Q6= Enter string to reverse:')
print(string[::-1])

# 7. Please write a program which count and print the numbers of each character in a string input by console
string = input('Q7= Enter string to count each character:')
dict = {}
for i in string:
    if i in dict.keys():
        dict[i] += 1
    else:
        dict[i] = 1
print(dict.items())
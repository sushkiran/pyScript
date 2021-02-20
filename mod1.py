def factors(num):
    odd = []
    even = []
    for i in range(1, num + 1):
        if num % i == 0:
            if i % 2 == 0:
                even.append(i)
            else:
                odd.append(i)
    return odd, even


def evens():
    result = []
    for num in range(1000, 3000):
        cnt = 0
        for i in range(0, len(str(num))):
            if int(str(num)[i]) % 2 == 0:
                cnt += 1
        if cnt == len(str(num)):
            result.append(num)
    return result


def sortme(str):
    return sorted(str.split())


def howMany(str):
    digit = 0
    alpha = 0
    special = 0
    for i in str:
        if i.isalpha():
            alpha += 1
        elif i.isdigit():
            digit += 1
        else:
            special += 1

    return digit, alpha, special


def isPali(str):
    str = str.casefold()
    if str != str[::-1]:
        return str + ' is Not a Palindrome'
    return str + ' is a Palindrome'


factors = factors(36)
howMany = howMany('Python@345')
print('Odd factors', factors[0], 'and Even factors', factors[1])
print('Numbers with all even digits', evens())
print('Sorted List', sortme('Hello how are you'))
print('Digits', howMany[0], 'Alphabets', howMany[1], 'Special Chars', howMany[2])
print(isPali('Sushvin'))
print(isPali('Nitin'))

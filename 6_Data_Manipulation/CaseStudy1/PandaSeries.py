import pandas as pd
import numpy as np

'''
6.1: From the raw data below create a Pandas Series
a) Print all elements in lower case
b) Print all the elements in upper case
c) Print the length of all the elements
'''
print('\n-- SERIES 1 --')
s1 = pd.Series(['Amit', 'Bob', 'Kate', 'A', 'b', np.nan, 'Car', 'dog', 'cat'])
print(s1.str.lower())
print(s1.str.upper())
print(s1.str.len())

'''
6.2: From the raw data below create a Pandas Series 
a) Print all elements after stripping spaces from the left and right
b) Print all the elements after removing spaces from the left only
c) Print all the elements after removing spaces from the right only
'''
print('\n-- SERIES 2 --')
s2 = pd.Series([' Atul', 'John ', ' jack ', 'Sam'])
print(s2.str.strip())
print(s2.str.lstrip())
print(s2.str.rstrip())

'''
6.3: - Create a series from the raw data below 
'India_is_big', 'Population_is_huge', np.nan, 'Has_diverse_culture'
a) split the individual strings wherever ‘_’ comes and create a list out of it.
b) Access the individual element of a list
c) Expand the elements so that all individual elements get splitted by ‘_’ 
and instead of list returns individual elements
'''
print('\n-- SERIES 3 --')
s3 = pd.Series(['India_is_big', 'Population_is_huge', np.nan, 'Has_diverse_culture'])
print(s3.str.split('_'))
print(s3[1])
x = s3.str.split('_')
z = []
for e in x:
    if type(e) is list:
        for y in e:
            z.append(y)
    else:
        z.append(e)

print(x)
print(z)

'''
6.4: Create a series and replace either X or dog with XX-XX
'A', 'B', 'C', 'AabX', 'BacX','', np.nan, 'CABA', 'dog', 'cat'
'''
print('\n-- SERIES 4 --')
s4 = pd.Series(['A', 'B', 'C', 'AabX', 'BacX', '', np.nan, 'CABA', 'dog', 'cat'])
s4 = s4.str.replace('X|dog', 'XX-XX', regex=True)
print(s4)

'''
6.5: Create a series and remove dollar from the numeric values '12', '-$10', '$10,000'
'''
print('\n-- SERIES 5 --')
s5 = pd.Series(['12', '-$10', '$10,000'])
s5 = s5.str.replace('$', '', regex=False)
print(s5)

'''
6.6:- Create a series and reverse all lower case words 'india 1998', 'big country', np.nan
'''
print('\n-- SERIES 6 --')
s6 = pd.Series(['india 1998', 'big country', np.nan])
na = [
    s if type(s) is not str
    else
    ' '.join(
        [
            i[::-1] if i.islower() else i for i in s.split()
        ]
    ) for s in s6
]
print(na)

'''
6.7: Create pandas series and print true if value is alphanumeric in series or 
false if value is not alpha numeric in series.
'1', '2', '1a', '2b', '2003c'
'''

print('\n-- SERIES 7 --')
s7 = pd.Series(['1', '2', '1a', '2b', '2003c', '$%^'])
print(s7.str.isalnum())


'''
6.8: Create pandas series and print true if value is containing ‘A’
'1', '2', '1a', '2b', 'America', 'VietnAm','vietnam', '2003c'
'''
print('\n-- SERIES 8 --')
s8 = pd.Series(['1', '2', '1a', '2b', 'America', 'VietnAm','vietnam', '2003c'])
print(s8.str.contains('A'))

'''
6.9: Create pandas series and print in three columns value 0 or 1 
if a or b or c exists in values 'a', 'a|b', np.nan, 'a|c'
'''
print('\n-- SERIES 9 --')
s9 = pd.Series(['a', 'a|b', np.nan, 'a|c'])
d9 = pd.DataFrame(s9, columns=['Series'])
da = pd.DataFrame(s9.str.contains('a'), columns=['a'])
db = pd.DataFrame(s9.str.contains('b'), columns=['b'])
dc = pd.DataFrame(s9.str.contains('c'), columns=['c'])
d9 = pd.concat([d9, da, db, dc], axis=1)
d9.set_index('Series', inplace=True)
d9 = d9.astype(int, errors='ignore')
print(d9)


'''
6.10: Create pandas dataframe having keys and ltable and rtable as below - 
'key': ['One', 'Two'], 'ltable': [1, 2] 
'key': ['One', 'Two'], 'rtable': [4, 5] 
Merge both the tables based of key
'''
print('\n-- SERIES 10 --')
data1 = {
    'key': ['One', 'Two'],
    'value': [1, 2]
}
data2 = {
    'key': ['One', 'Two'],
    'value': [4, 5]
}
ltable = pd.DataFrame(data1)
rtable = pd.DataFrame(data2)
print(ltable.merge(rtable, on='key'))

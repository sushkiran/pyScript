import pandas as pd
import numpy as np

'''
1: From the raw data below create a data frame
'''

data = {
    'first_name': ['Jason', 'Molly', 'Tina', 'Jake', 'Amy'],
    'last_name': ['Miller', 'Jacobson', ".", 'Milner', 'Cooze'],
    'age': [42, 52, 36, 24, 73],
    'preTestScore': [4, 24, 31, ".", "."],
    'postTestScore': ["25,000", "94,000", 57, 62, 70]
}

df = pd.DataFrame(data)

'''
2: Save the dataframe into a csv file as example.csv
'''

df.to_csv('example.csv')

'''
3: Read the example.csv and print the data frame
'''

df = pd.read_csv('example.csv')
print(df.head())

'''
4: Read the example.csv without column heading
'''

print(df.to_string(header=False))

'''
5: Read the example.csv and make the index columns as 'First Name’ and 'Last Name'
'''

df.set_index(['first_name', 'last_name'])
print(df)

'''
6: Print the data frame in a Boolean form as True or False. True for Null/ NaN values and false for non-null values
'''

print(df.isna())

'''
7: Read the dataframe by skipping first 3 rows and print the data frame
'''

print(df.loc[3:,])

'''
8: Load a csv file while interpreting "," in strings around numbers as thousands separators. 
Check the raw data 'postTestScore' column has, as thousands separator. Comma should be ignored while reading the data. 
It is default behaviour, but you need to give argument to read_csv function which makes sure commas are ignored
'''

df = pd.read_csv('example.csv',usecols=range(6))
print(df)
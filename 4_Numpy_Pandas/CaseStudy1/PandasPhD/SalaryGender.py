"""
1. Extract data from the given PandasPhD CSV file and store the data from each column in a separate NumPy array
2. Find: (1) The number of men with a PhD (2) The number of women with a PhD
3. Store the “Age” and “PhD” columns in one DataFrame
    and delete the data of all people who don’t have a PhD from PandasPhD CSV file.
4. Calculate the total number of people who have a PhD degree from PandasPhD CSV file.
"""

import numpy as np
import pandas as pd

'''
1. Extract data from the given PandasPhD CSV file and store the data from each column in a separate NumPy array
'''

df = pd.read_csv('SalaryGender.csv')

df.update(df['Gender'].replace({0: 'Male', 1: 'Female'}))
df.update(df['PhD'].replace({0: 'No', 1: 'Yes'}))

np_sal = np.asarray(df['Salary'])
np_gender = np.asarray(df['Gender'])
np_age = np.asarray(df['Age'])
np_PhD = np.asarray(df['PhD'])

'''
2. Find: (1) The number of men with a PhD (2) The number of women with a PhD
'''

print('Distribution of PhD, Gender-wise:')
print(df.query('PhD=="Yes"').groupby('Gender').size())

male = df.apply(lambda x: True if x.PhD == "Yes" and x.Gender == 'Male' else False, axis=1)
print('Total number of men with a PhD: ', male[male].shape[0])

female = df.apply(lambda x: True if x.PhD == "Yes" and x.Gender == 'Female' else False, axis=1)
print('Total number of women with a PhD: ', female[female].shape[0])

'''
3. Store the “Age” and “PhD” columns in one DataFrame
   and delete the data of all people who don’t have a PhD from PandasPhD CSV file.
'''

new_df = pd.DataFrame({'Age': np_age, 'PhD': np_PhD})
# print(new_df)

cond = df.PhD == 'No'
df.drop(df[cond].index, inplace=True)
# print(df)

'''
4. Calculate the total number of people who have a PhD degree from PandasPhD CSV file.
'''

print('\nTotal number of people with PhD degrees: ', df.shape[0])

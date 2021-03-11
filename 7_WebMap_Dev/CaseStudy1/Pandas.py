import pandas as pd
import numpy as np

print('\nCreate a pandas dataframe having following structure')
dataset = {
    'float_col': [0.1, 0.2, 0.2, 10.1, np.nan],
    'int_col': [1, 2, 6, 8, -1],
    'str_col': ['a', 'b', None, 'c', 'a']
}

df = pd.DataFrame(dataset)
print(df)

print('\nFilter columns float_col, int_col from the dataframe in one query')
print(df[['float_col', 'int_col']])
print(df.iloc[:, :-1])

print('\nFilter records from float_col having value greater than 0.15')
float_series = df['float_col']
print(float_series[float_series > 0.15])

print('\nFilter records from float_col having value equal to 0.1')
print(float_series[float_series == 0.1])

print('\nFilter records from dataframe having float_col greater than 0.1 AND int_col greater than 2')
print(df[(df.float_col > 0.1) & (df.int_col > 2)])

print('\nFilter records from dataframe having float_col greater than 0.1 OR int_col greater than 2')
print(df[(df.float_col > 0.1) | (df.int_col > 2)])

print('\nFilter records from dataframe which satisfies the conditions float_col not greater than 0.1')
print(df[~(df.float_col > 0.1)])

print('\nCreate a new data frame in which column int_col is renamed to new_name')
new_df = df.copy()
new_df.columns = [item.replace('int_col','new_name') for item in df.columns]
print(new_df)

print('\nModify the existing data frame and rename the column int_col to new_name')
df.columns = [item.replace('int_col','new_name') for item in df.columns]
print(df)

print('\nDrop the rows where any value is missing from the data frame')
print(df.dropna())

print('\nChange the missing value in column float_col as mean value of the float_col')
df.float_col = df.float_col.fillna(df.float_col.mean())
print(df)

print('\nPrefix all values of str_col with \'map_\' and drop the missing values. ')
dropped = df.copy()
dropped.dropna(inplace=True)
dropped['str_col'] = dropped['str_col'].apply(lambda x: 'map_' + x)
print(dropped)

print('\nfind the covariance of float_col and int_col')
print(df.cov())

print('\nfind the correlation of float_col and int_col')
print(df.corr())

print('\nCreate a data frame \'other\' having columns some_val and str_col')
other_dataset = {
    'some_val': [1, 2],
    'str_col': ['a', 'b']
}
other = pd.DataFrame(other_dataset)
print(other)

print('\nINNER JOIN of both dataframes')
print(df.merge(other, how='inner'))

print('\nOUTER JOIN of both dataframes')
print(df.merge(other, how='outer'))

print('\nLEFT JOIN of both dataframes')
print(df.merge(other, how='left'))

print('\nRIGHT JOIN of both dataframes')
print(df.merge(other, how='right'))

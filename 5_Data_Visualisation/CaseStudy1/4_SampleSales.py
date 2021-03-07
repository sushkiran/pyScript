"""
Create csv file from the data below and read in pandas data frame
1. Reading Data
2. Describe the data on the unit price
3. filter the data: Create new dataframe having columns 'name','net_price','date'
    and group all the records according to name
4. Plotting graph: Plot the graph after calculating total sales by each customer.
    Customer name should be on x axis and total sales in y axis.
"""

import matplotlib.pyplot as plt
import pandas as pd

# 1. read CSV
df = pd.read_csv('sample-salesv2.csv')

# 2. Describe data on unit price
print(df['unit price'].describe())

# 3. Create new data frame + grouping
new_df = df[['name', 'net_price', 'date']]
sales_df = new_df.groupby('name').sum('net_price').reset_index()
print(sales_df)

# 4 Graph
plt.plot(pd.Series(sales_df['name']), pd.Series(sales_df['net_price']))

plt.xlabel('Customer Name')
plt.ylabel('Total Sales')
plt.xticks(rotation=50)

plt.show()
plt.close()

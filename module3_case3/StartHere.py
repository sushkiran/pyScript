"""
Business challenge/requirement
GoodsKart—largest ecommerce company of Indonesia with revenue of $2B+ acquired another ecommerce company FairDeal.
FairDeal has its own IT system to maintain records of customer, sales etc.
For ease of maintenance and cost savings GoodsKart is integrating customer databases of both the organizations
hence customer data of FairDeal has to be converted in GoodsKartCustomer Format.

Key issues
GoodsKart customer data has more fields than in FairDeal customer data.
Hence FairDeal data needs to be split and stored in GoodsKart Customer Object Oriented Data Structure

Approach to Solve
1.Read FairDealCustomerData.csv
2.Name field contains full name –use regular expression to separate title, first name, last name
3.Store the data in Customer Class
4.Create Custom Exception –CustomerNotAllowedException
5.Pass a customer to function "createOrder" and throw CustomerNotAllowedException in case of blacklisted value is 1
"""

import re
import FairDeal

black_list = []
white_list = []
with open('FairDealCustomerData.csv') as file:
    for row in file:
        split_arr = re.split('[,.]', row)
        data = list(map(lambda z: z.strip(), split_arr))
        fd_cust = FairDeal.Customer(title=data[1], first_nm=data[2], last_nm=data[0], b_listed=(data[3] == '1'))

        try:
            FairDeal.create_order(fd_cust)
            white_list.append(fd_cust)
        except FairDeal.CustomerNotAllowedException:
            black_list.append(fd_cust)


print('Below List of FairDeal customers are black-Listed')
text = '{} {} {}'
for b in black_list:
    print(text.format(b.title, b.first_name, b.last_name))

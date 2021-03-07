"""
1. Plot Total Sales Per Month for Year 2011. How the total sales have increased over months in Year 2011.
Which month has lowest Sales?
2. Plot Total Sales Per Month for Year 2011 as Bar Chart. Is Bar Chart Better to visualize than Simple Plot?
3. Plot Pie Chart for Year 2011 Country Wise. Which Country contributes highest towards sales?
4. Plot Scatter Plot for the invoice amounts and see the concentration of amount.
In which range most of the invoice amounts are concentrated

Enhancements for code
1. Change the bar chart to show the value of bar
2. In Pie Chart Play With Parameters shadow=True, startangle=90 and see how different the chart looks
3. In scatter plot change the color of Scatter Points
"""

import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('BigMartSalesData.csv')
sales_df = df[df.Year == 2011].groupby('Month').sum().reset_index()
sales_df = sales_df.round(2)

fig, ax = plt.subplots(2, 2, figsize=(10, 5))
fig.tight_layout(h_pad=2)

'''
1. Plot Total Sales Per Month for Year 2011. How the total sales have increased over months in Year 2011.
# Question: Which month has lowest Sales?
# Answer: Month 1 has the lowest Sales of 550K amount
'''
plt.subplot(2, 2, 1)
plt.plot(sales_df['Month'], sales_df['Amount'])
plt.title('Total Sales Line Plot')

print(sales_df.min())

'''
2. Plot Total Sales Per Month for Year 2011 as Bar Chart. 
ENH(1) Change the bar chart to show the value of bar
# Question: Is Bar Chart Better to visualize than Simple Plot?
# Answer Yes for this Data Set.
'''
plt.subplot(2, 2, 2)
plt.bar(sales_df['Month'], sales_df['Amount'])
plt.title('Total Sales Bar Graph')


'''
3. Plot Pie Chart for Year 2011 Country Wise. 
ENH(2): Play With Parameters shadow=True, startangle=90 and see how different the chart looks
# Question: Which Country contributes highest towards sales?
# Answer: United Kingdom
'''
country_sales_df = df[df.Year == 2011].groupby('Country').sum().reset_index()

plt.subplot(2, 2, 3)
plt.pie(country_sales_df['Amount'], labels=country_sales_df['Country'], shadow=True, startangle=90)
plt.title('Country Wise Pie')

'''
4. Plot Scatter Plot for the invoice amounts and see the concentration of amount.
ENH(3) In scatter plot change the color of Scatter Points
# Question: In which range most of the invoice amounts are concentrated
# Answer: Invoice amount concentration is less than 1 million.
'''
plt.subplot(2, 2, 4)
plt.scatter(sales_df['Month'], sales_df['Amount'], c=sales_df['Month'])
plt.title('Invoice Scatter')

plt.subplots_adjust(top=0.85, bottom=0.1, left=0.08)
plt.suptitle('BIG Mart Sales Representation', fontsize=14)

plt.show()
plt.close()

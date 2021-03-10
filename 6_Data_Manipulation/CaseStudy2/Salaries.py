"""
Business challenge/requirement
SFO Public Department - referred to as SFO has captured all the salary data of its employees from year 2011-2014.
Now we are in year 2015 and the organization is facing some financial crisis. As first step HR wants to rationalize
employee cost to save payroll budget. You have to do data manipulation and analysis on the salary data to answer
specific questions for cost savings.

Approach:
1. Compute how much total salary cost has increased from year 2011 to 2014
2. Which Job Title in Year 2014 has highest mean salary?
3. How much money could have been saved in Year 2014 by stopping OverTimePay?
4. Which are the top 5 common job in Year 2014 and how much do they cost SFO ?
5. Who was the top earning employee across all the years?

Code Enhancements:
6. Which are the last 5 common job in Year 2014 and how much do they cost SFO?
7. In year 201 OverTimePay was what percentage of TotalPayBenefits
8. Which Job Title in Year 2014 has lowest mean salary?
"""

import pandas as pd
import numpy as np

sal_df = pd.read_csv('Salaries.csv', low_memory=False)
year_2014 = sal_df['Year'] == 2014

# 1. Compute how much total salary cost has increased from year 2011 to 2014
yearly_sum = sal_df.groupby('Year')['TotalPayBenefits'].sum()
increase = yearly_sum.max() - yearly_sum.min()
pct_change = 100 * (increase / yearly_sum.min())
text = '1. Total Salary Cost increased by {:.2f}% from 2011 to 2014.'
print(text.format(pct_change))

# 2. Which Job Title in Year 2014 has highest mean salary?
mean_sal_2014 = sal_df[year_2014].groupby('JobTitle')['TotalPayBenefits'].mean()
text = '2. The Job Title \"{}\" earned the highest mean salary of Rs.{:,.2f} in 2014.'
print(text.format(mean_sal_2014.idxmax(), mean_sal_2014.max()))

# 3. How much money could have been saved in Year 2014 by stopping OverTimePay?
overtime_2014 = sal_df[year_2014]['OvertimePay'].sum()
text = '3. A total sum of Rs.{:,.2f} could have been saved in Year 2014 by stopping OverTimePay'
print(text.format(overtime_2014))

# 4. Which are the top 5 common job in Year 2014 and how much do they cost SFO ?
columns = ['JobTitle', 'TotalPayBenefits']
jobs_2014 = sal_df[year_2014][columns]
jobs_2014.set_index('JobTitle', inplace=True)
top_jobs_2014 = jobs_2014.sort_values(by='TotalPayBenefits', ascending=False).head(5)
text = '4. The list of top 5 jobs of 2014 is shown below. Their total cost to the SFO is Rs.{:,.2f}/-'
print(text.format(np.array(top_jobs_2014['TotalPayBenefits']).sum()))
print('\t', list(top_jobs_2014.index))

# 5. Who was the top earning employee across all the years?
emp_sal = sal_df.groupby('EmployeeName')['TotalPayBenefits'].sum()
text = '5. The top earning employee across all years is \"{}\" with total salary of Rs.{:,.2f}/-'
print(text.format(emp_sal.idxmax(), emp_sal.max()))

# 6. Which are the last 5 common job in Year 2014 and how much do they cost SFO?
last_jobs_2014 = jobs_2014.sort_values(by='TotalPayBenefits', ascending=False).tail(5)
text = '6. The list of last 5 jobs of 2014 is shown below. Their total cost to the SFO is Rs.{:,.2f}/-'
print(text.format(np.array(last_jobs_2014['TotalPayBenefits']).sum()))
print('\t', list(last_jobs_2014.index))

# 7. In year 2014 OverTimePay was what percentage of TotalPayBenefits
overtime_2014 = sal_df[year_2014]['OvertimePay'].mean()
total_pay_2014 = sal_df[year_2014]['TotalPayBenefits'].mean()
text = '7. In the year 2014 the OverTimePay component was {:.2f}% of TotalPayBenefits'
print(text.format(100 * (overtime_2014 / total_pay_2014)))

# 8. Which Job Title in Year 2014 has lowest mean salary?
low_mean_sal_2014 = sal_df[year_2014].groupby('JobTitle')['TotalPayBenefits'].mean()
text = '8. The Job Title \"{}\" earned the lowest mean salary of Rs.{:,.2f} in 2014.'
print(text.format(low_mean_sal_2014.idxmin(), low_mean_sal_2014.min()))

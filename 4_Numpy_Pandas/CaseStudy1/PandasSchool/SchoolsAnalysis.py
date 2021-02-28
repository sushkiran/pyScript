"""
15. Analyse various school outcomes in Tennessee using pandas. Suppose you are a public school administrator.
Some schools in your state of Tennessee are performing below average academically. Your superintendent,
under pressure from frustrated parents and voters, approached you with the task of understanding why these schools
are under-performing.

To improve school performance, you need to learn more about these schools and their students, just as a business
needs to understand its own strengths and weaknesses and its customers. Though you are eager to build an impressive
explanatory model, you know the importance of conducting preliminary research to prevent possible pitfalls
or blind spots. Thus, you engage in a thorough exploratory analysis, which includes: a lit review, data collection,
descriptive and inferential statistics, and data visualization.
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sn

"""
-------------------------
Phase 1 - Data Collection
-------------------------
Here is a data of every public school in middle Tennessee. The data also includes various demographic,
school faculty, and income variables. You need to convert the data into useful information.
• Read the data in pandas data frame
• Describe the data to find more details
"""

print('\n--Phase 1--')
df = pd.read_csv('middle_tn_schools.csv')
print(df.describe())

"""
--------------------------------------
Phase 2 - Group data by school ratings
--------------------------------------
Choose indicators that describe the student body (for example, reduced_lunch) or school administration 
(stu_teach_ratio) hoping they will explain school_rating. The reduced_lunch is a variable measuring the 
average percentage of students per school enrolled in a federal program that provides lunches for students 
from lower-income households. In short, reduced_lunch is a good proxy for household income. 
• Isolate ‘reduced_lunch’ and group the data by ‘school_rating’ using pandas groupby method
• and then use describe on the re-shaped data
"""

print('\n--Phase 2--')
isolated_df = df.copy()
isolated_df.pop('reduced_lunch')
print(isolated_df.groupby('school_rating').size())
print(isolated_df.describe())

"""
------------------------------
Phase 3 – Correlation analysis
------------------------------
Find the correlation between ‘reduced_lunch’ and ‘school_rating’. The values in the correlation matrix table
will be between -1 and 1. A value of -1 indicates the strongest possible negative correlation, meaning as one
decreases the other increases. And a value of 1 indicates the opposite.
"""

print('\n--Phase 3--')
corr_df = df[['reduced_lunch', 'school_rating']]
corr_matrix = corr_df.corr()
print(corr_matrix)

"""
----------------------
Phase 4 – Scatter Plot
----------------------
Find the relationship between school_rating and reduced_lunch, Plot a graph with the two variables on a scatter plot.
Each dot represents a school. The placement of the dot represents that school's rating (Y-axis) and the percentage
of its students on reduced lunch (x-axis). The downward trend line shows the negative correlation between
school_rating and reduced_lunch (as one increases, the other decreases). 

The slope of the trend line indicates how much school_rating decreases as reduced_lunch increases. A steeper slope 
would indicate that a small change in reduced_lunch has a big impact on school_rating while a more horizontal slope 
would indicate that the same small change in reduced_lunch has a smaller impact on school_rating.
"""

corr_df.plot(kind='scatter', y='school_rating', x='reduced_lunch')
# plt.show()

"""
----------------------------
Phase 5 – Correlation Matrix
----------------------------
An efficient graph for assessing relationships is the correlation matrix, as seen below;
its color-coded cells make it easier to interpret than the tabular correlation matrix above.
Red cells indicate positive correlation; blue cells indicate negative correlation;
white cells indicate no correlation. The darker the colors, the stronger the correlation (positive or negative)
between those two variables. Draw a graph of correlation matrix having all important fields of data frame.
"""

sn.heatmap(corr_matrix, annot=True)
plt.show()

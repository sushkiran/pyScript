"""
Business challenge/requirement
You are a data analyst with University of Cal USA.The University has data of Math, Physics and Data Structure score of
sophomore students. This data is stored in different files. The University has hired a data science company to do
analysis of scores and find if there is any correlation of score with age, ethnicity etc. Before the data is given
to the company you have to do data wrangling.

Approach to Solve:
1. Read the three csv files which contains the score of same students in term1 for each Subject
2. Remove the name and ethnicity column (to ensure confidentiality)
3. Fill missing score data with zero
4. Merge the three files
5. Change Sex(M/F) Column to 1/2 for further analysis
6. Store the data in new file – ScoreFinal.csv

Enhancements for code (You can try these enhancements in code)
1. Convert ethnicity to numerical value
2. Fill the missing score for a student to the average of the class
"""

import pandas as pd

# 1. Read the three csv files which contains the score of same students in term1 for each Subject
df_data = pd.read_csv('DSScoreTerm1.csv')
df_math = pd.read_csv('MathScoreTerm1.csv')
df_phys = pd.read_csv('PhysicsScoreTerm1.csv')

# 4. Merge the three files
df = df_data.append(df_math).append(df_phys)
df.reset_index(drop=True, inplace=True)

# 2. Remove the name and ethnicity column (to ensure confidentiality)
# 3. Fill missing score data with zero
df = df.drop(['Name', 'Ethinicity'], axis=1).fillna(0)

# 5. Change Sex(M/F) Column to 1/2 for further analysis
df.Sex = df.Sex.apply(lambda x: 1 if x == 'M' else 2)

# 6. Store the data in new file – ScoreFinal.csv
df.to_csv('ScoreFinal.csv')

# Enhancement 1. Convert ethnicity to numerical value
# print(sorted(df_data.Ethinicity.unique()))
race = {
    'African American': 1,
    'European American': 2,
    'Hispanic': 3,
    'White American': 4
}
df_data.Ethinicity = df_data.Ethinicity.map(race)
df_math.Ethinicity = df_math.Ethinicity.map(race)
df_phys.Ethinicity = df_phys.Ethinicity.map(race)

# Enhancement 2. Fill the missing score for a student to the average of the class
df_data = df_data.fillna(df_data.Score.mean())
df_math = df_math.fillna(df_math.Score.mean())
df_phys = df_phys.fillna(df_phys.Score.mean())

# print(df_data, df_phys, df_math)

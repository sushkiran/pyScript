import datetime as dt
import pandas as pd
import numpy as np
from numpy import random
import matplotlib.pyplot as plt

"""
-----------------------------
Definitions of the Constants
----------------------------- 
"""

end_date = dt.date(2021, 7, 1)  # 1st July 2021
calypso_team = np.array(['Naveen', 'Sushvin', 'Divik', 'Kapil'])
group_members = {
    'A': ['Naveen'],
    'B': ['Kapil', 'Sushvin'],
    'C': ['Divik']
}
group_names = tuple(group_members.keys())  # ordered, unchangeable hence tuple

base_record = {
    'Wk_start': [dt.date(2021, 3, 1)],
    'Group': ['B'],
    'Cal_Primary': ['Naveen'],
    'Cal_Standby': ['Sushvin'],
    'BAS_Finance': ['Divik']
}

"""
---------------------
Function Definitions
--------------------- 
"""


def next_group(grp):
    index = group_names.index(str(grp)) + 1
    if index < len(group_names):
        return group_names[index]
    else:
        # reset index to 0
        return group_names[0]


def choose_member(exclude_list):
    mask = []
    for member in calypso_team:
        mask.append(member not in exclude_list)
    return random.choice(list(calypso_team[mask]))


def process():
    df = pd.DataFrame(base_record)
    date = df['Wk_start'][0]
    group = df['Group'][0]
    seven = dt.timedelta(7)

    while date + seven < end_date:
        date += seven
        group = next_group(group)
        prev_index = len(df.index) - 1

        exclude_me = list(group_members[group])
        exclude_me.append(df['Cal_Primary'][prev_index])
        primary = choose_member(exclude_me)

        exclude_me = [primary, df['BAS_Finance'][prev_index]]
        bas = choose_member(exclude_me)

        exclude_me = [primary, bas, df['Cal_Standby'][prev_index]]
        standby = choose_member(exclude_me)

        df.loc[len(df.index)] = [date, group, primary, standby, bas]

    distribution = df[['Cal_Primary', 'Cal_Standby', 'BAS_Finance']].apply(pd.Series.value_counts)
    unique_dist = set(distribution.values.flat)

    boolean_result = all(each_val in (4, 5) for each_val in unique_dist)
    if boolean_result:
        print(df, distribution)
        df.to_excel('c5_rota.xlsx', index=False)

        plt.figure(figsize=(3, 3))
        values = distribution.sum(axis=1)
        labels = np.asarray(distribution.index.values.flat)

        plt.pie(values, labels=labels)
        plt.show()
    else:
        process()


if __name__ == '__main__':
    process()

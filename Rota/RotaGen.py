import datetime as dt
import pandas as pd
import numpy as np
from numpy import random

"""
-----------------------------
Definitions of the Constants
----------------------------- 
"""

num_weeks = 20
calypso_team = np.array(['Naveen', 'Sushvin', 'Divik', 'Kapil'])
group_members = {
    'A': ['Divik'],
    'B': ['Kapil', 'Sushvin'],
    'C': ['Naveen']
}
group_names = tuple(group_members.keys())  # ordered, unchangeable hence tuple

base_record = {
    'Wk_start': [dt.datetime(2021, 3, 1)],
    'Group': ['B'],
    'Cal_Primary': ['Naveen'],
    'Cal_Standby': ['Sushvin'],
    'BAS_Finance': ['Divik']
}
df = pd.DataFrame(base_record)

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


if __name__ == '__main__':
    date = df['Wk_start'][0]
    group = df['Group'][0]

    for num in range(num_weeks):

        date += dt.timedelta(7)
        group = next_group(group)

        exclude_me = list(group_members[group])
        if len(exclude_me) < 3:
            prev_primary = df['Cal_Primary'][len(df.index) - 1]
            exclude_me.append(prev_primary)
        primary = choose_member(exclude_me)

        exclude_me = list(group_members[group])
        exclude_me.append(primary)
        if len(exclude_me) < 3:
            prev_bas = df['BAS_Finance'][len(df.index) - 1]
            exclude_me.append(prev_bas)
        bas = choose_member(exclude_me)

        exclude_me = [primary, bas]
        if len(exclude_me) < 3:
            prev_standby = df['Cal_Standby'][len(df.index) - 1]
            exclude_me.append(prev_standby)
        standby = choose_member(exclude_me)

        df.loc[len(df.index)] = [date, group, primary, standby, bas]

    print(df)
    df.to_excel('c5_rota.xlsx')

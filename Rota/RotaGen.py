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
    'BAS_FinC': ['Divik']
}
df = pd.DataFrame(base_record)

"""
---------------------
Function Definitions
--------------------- 
"""


def get_next_group(grp):
    index = group_names.index(str(grp)) + 1
    if index < len(group_names):
        return group_names[index]
    else:
        # reset index to 0
        return group_names[0]


def get_random_member(exclude_me):
    mask = []
    for member in calypso_team:
        mask.append(member not in exclude_me)
    return random.choice(list(calypso_team[mask]))


def get_next_primary(group):
    exclude_me = group_members[group]
    return get_random_member(exclude_me)


def get_next_standby(primary):
    exclude_me = [primary]
    return get_random_member(exclude_me)


def get_next_bas(group, primary, standby):
    exclude_me = [primary, standby, group_members[group]]
    return get_random_member(exclude_me)


if __name__ == '__main__':
    date = df['Wk_start'][0]
    group = df['Group'][0]

    for num in range(num_weeks):
        date += dt.timedelta(7)
        group = get_next_group(group)
        primary = get_next_primary(group)
        standby = get_next_standby(primary)
        bas = get_next_bas(group, primary, standby)
        df.loc[len(df.index)] = [date, group, primary, standby, bas]

    print(df)
    df.to_excel('c5_rota.xlsx')

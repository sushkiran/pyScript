import datetime as dt
import pandas as pd
from pandas.core.common import flatten

name = 'Sushvin'
out_df_columns = ['Date', 'Reference', 'Amount']
filename = '{}_{}_to_{}.xlsx'

# 1-march to 1-april
from_date = dt.date(2021, 3, 1)
to_date = dt.date(2021, 4, 1)

# convert source to dataframe
df = pd.read_excel('c5_rota.xlsx')

# generate calypso standby claim
my_cal_dates = []
for x in df[df['Cal_Standby'] == name]['Wk_start']:
    my_cal_dates.append(pd.date_range(x, x + dt.timedelta(4)).values)

my_cal_dates = list(flatten(my_cal_dates))
filtered_cal = [pd.Timestamp(date) for date in my_cal_dates
                if pd.Timestamp(from_date) <= pd.Timestamp(date) <= pd.Timestamp(to_date)]

my_cal_df = pd.DataFrame(columns=out_df_columns)
my_cal_df['Date'] = pd.Series(filtered_cal)
my_cal_df = my_cal_df.assign(Reference='Calypso Standby Support')
my_cal_df = my_cal_df.assign(Amount='30')

# generate bas standby claim
my_bas_dates = []
for x in df[df['BAS_Finance'] == name]['Wk_start']:
    my_bas_dates.append(pd.date_range(x, x + dt.timedelta(4)).values)

my_bas_dates = list(flatten(my_bas_dates))
filtered_bas = [pd.Timestamp(date) for date in my_bas_dates
                if pd.Timestamp(from_date) <= pd.Timestamp(date) <= pd.Timestamp(to_date)]

my_bas_df = pd.DataFrame(columns=out_df_columns)
my_bas_df['Date'] = pd.Series(filtered_bas)
my_bas_df = my_bas_df.assign(Reference='BAS Standby Support')
my_bas_df = my_bas_df.assign(Amount='30')

# combine both claims
result_df = my_cal_df.append(my_bas_df)
result_df.reset_index(inplace=True)
del result_df['index']
print(result_df)


# write combines claim to out-file
out_file_name = filename.format(name, str(from_date), str(to_date))
result_df.to_excel(out_file_name, index=False)

# TODO
'''
1. file name from date & to date should come from result_df, first & last records.
2. result_df should be sorted by Date.
3. Excel output should be limited to only Date, to truncate the timestamps.
4. May need to rename variable names to make more logical.
5. testing on smaller & bigger date ranges.
6. negative testing, i.e. No calypso support and/or no bas support.
7. Simplify cal_df, bas_df, resultant_df, if possible (make it in one)
'''
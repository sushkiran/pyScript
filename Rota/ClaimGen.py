import datetime as dt
import pandas as pd
from pandas.core.common import flatten

''' 
---------------------
Constants Definitions
---------------------
'''
out_df_columns = ['Date', 'Reference', 'Amount']
filename = '{}_{}_to_{}.xlsx'

'''
----------------
INPUTS in Phase2
----------------
'''
# 1-march to 1-april
from_date = dt.date(2021, 3, 1)
to_date = dt.date(2021, 4, 1)

# candidate name
name = 'Sushvin'

'''
--------------------
FUNCTION definitions
--------------------
'''


def generate(for_what):
    # using list comprehension to initialize all dates
    date_arr = [
        pd.date_range(start=x, periods=5).values
        for x in df[df[for_what] == name]['Wk_start']
    ]
    date_arr = list(flatten(date_arr))

    # using list comprehension to initialize all WANTED dates
    wanted = [
        pd.Timestamp(date) for date in date_arr
        if pd.Timestamp(from_date) <= pd.Timestamp(date) <= pd.Timestamp(to_date)
    ]

    out_df = pd.DataFrame(columns=out_df_columns)
    out_df['Date'] = pd.Series(wanted)

    ref_str = 'Calypso Standby Support' if for_what == 'Cal_Standby' else 'BAS Standby Support'
    out_df = out_df.assign(Reference=ref_str)
    out_df = out_df.assign(Amount='30')

    return out_df


if __name__ == '__main__':
    # convert ROTA excel doc to dataframe
    df = pd.read_excel('c5_rota.xlsx')

    result_df = generate('Cal_Standby')
    result_df = result_df.append(generate('BAS_Finance'), ignore_index=True)
    result_df.sort_values(by='Date')
    print(result_df)

    # write combines claim to out-file
    out_file_name = filename.format(name, str(from_date), str(to_date))
    result_df.to_excel(out_file_name, index=False)

# TODO
'''
1. file name from date & to date should come from result_df, first & last records.
3. Excel output should be limited to only Date, to truncate the timestamps.
5. testing on smaller & bigger date ranges.
6. negative testing, i.e. No calypso support and/or no bas support.
'''

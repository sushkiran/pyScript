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
from_date = dt.date(2021, 2, 1)
to_date = dt.date(2021, 7, 1)

# candidate name
name = 'Kapil'

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
    out_df = out_df.assign(Amount=30)

    return out_df


if __name__ == '__main__':
    # convert ROTA excel doc to dataframe
    df = pd.read_excel('c5_rota.xlsx')

    result_df = generate('Cal_Standby')
    result_df = result_df.append(generate('BAS_Finance'), ignore_index=True)
    result_df = result_df.sort_values(by='Date')
    result_df.reset_index(drop=True, inplace=True)

    begin = result_df['Date'].min().strftime('%d-%m-%Y')
    end = result_df['Date'].max().strftime('%d-%m-%Y')

    result_df['Date'] = pd.to_datetime(result_df['Date']).apply(lambda x: x.strftime('%a %d-%m-%Y'))
    result_df.loc[len(result_df.index)] = ['', 'Total', result_df['Amount'].sum()]
    print(result_df)

    # write combined claim to out-file
    out_file_name = filename.format(name, begin, end)
    result_df.to_excel(out_file_name, index=False)
    print(out_file_name)


from datetime import datetime

from pandas.core.frame import DataFrame

import file_operations
import flow
import REST_operations as rest
import pandas as pd

if __name__ == "__main__":
    data = file_operations.read_excel('input/Upay example- 1.xlsx')
    df_temp = []
    sites_array = ['Norton Canes', 'Stafford', 'Tibshelf']
    units_array = ['Costa Coffee', 'FFC', 'WHSmiths', 'Chozen', 'Drive Thru', 'Leon']
    site = ""
    unit = ""
    sum_transaction_value = 0
    sum_transaction_charge = 0
    sum_standard_charge = 0
    sum_service_charge = 0

    # Remove pandas column
    for col in data.columns:
        if col.startswith('Unnamed'):
            data.drop(col, axis=1, inplace=True)


    for row in data.itertuples():
        # if row.Type contains 'Norton Canes'
        if any(x in row.Type for x in sites_array):
            site = row.Type[5:]
        if any(x in row.Type for x in units_array):
            unit = row.Type[6:]
        row = row + (site,unit)
        df_temp.append(row)

    df = pd.DataFrame(df_temp)

    for row in df.itertuples():
        for site in sites_array:
            for unit in units_array:


    # print(df)
    # DataFrame.to_csv(df, 'output/output.csv', index=False)
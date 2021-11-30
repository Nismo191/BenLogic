from datetime import datetime

from pandas.core.frame import DataFrame

from numpy import NaN, nan

import file_operations
import flow
import REST_operations as rest
import pandas as pd

class Unit():
    def __init__(self, site, unit, tVal, tCharge, standCharge, serviceCharge,):
        self.site = site
        self.unit = unit
        self.sum_transaction_value = tVal
        self.sum_transaction_charge = tCharge
        self.sum_standard_charge = standCharge
        self.sum_service_charge = serviceCharge


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
    totals = []

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
        if pd.isna(row._3):
            df.drop(row.Index, axis=0, inplace=True)

    df = df.rename({'_1': 'Type', '2': 'Scheme', '3': 'TCount', '4': 'TVal', '5': 'Standard Charge Rate', '6': 'Standard Charge Value', '7': 'Service Charge Rate', '8': 'Service Charge Value', '9': 'Site', '10': 'Unit'}, axis=1)

    # print(df.query('10 == Norton Canes')['5'].sum())


        # for site in sites_array:
        #     sum_transaction_value = 0
        #     sum_transaction_charge = 0
        #     sum_standard_charge = 0
        #     sum_service_charge = 0
        #     for unit in units_array:
        #         sum_transaction_value += row._4
        #         sum_transaction_charge += row._6
        #         sum_standard_charge += row._8
        #     sum_service_charge = (sum_standard_charge/100)*20
        #     totals.append(Unit(site, unit, sum_transaction_value, sum_transaction_charge, sum_standard_charge, sum_service_charge))

    # print(a)


    # print(df)
    DataFrame.to_csv(df, 'output/output.csv', index=False)


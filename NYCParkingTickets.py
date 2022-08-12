import dask.dataframe as dd

import pandas as pd


df = dd.read_csv("Parking_Violations_Issued_-_Fiscal_Year_2017.csv")

import testutility as util
config_data = util.read_config_file("NYC_Parking_Tickets.yaml")


file_type = config_data['file_type']
source_file = "./" + config_data['file_name'] + f'.{file_type}'
df = pd.read_csv(source_file,config_data['inbound_delimiter'])


util.col_header_val(df,config_data)


if util.col_header_val(df,config_data)==0:
    print("validation failed")
else:
    print("col validation passed")


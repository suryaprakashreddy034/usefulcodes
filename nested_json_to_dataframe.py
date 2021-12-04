from copy import deepcopy
import pandas as pd
import json
import numpy as np
import re
import sys
from google.cloud import storage
import pandas as pd
from pandas.io import gbq

test_Scenario="TS_Symedical_InitialLoad_008 - To validate the count of records between the files in GCS archive folder and GCS source file landing for Symedical"
print(test_Scenario)

#source file path
input_path1=input("Enter source File Path")#

# archive file path
input_path2=input("Enter archive File Path")#


def cross_join(left, right):
    new_rows = [] if right else left
    for left_row in left:
        for right_row in right:
            temp_row = deepcopy(left_row)
            for key, value in right_row.items():
                temp_row[key] = value
            new_rows.append(deepcopy(temp_row))
    return new_rows


def flatten_list(data):
    for elem in data:
        if isinstance(elem, list):
            yield from flatten_list(elem)
        else:
            yield elem


def json_to_dataframe(data_in):
    def flatten_json(data, prev_heading=''):
        if isinstance(data, dict):
            rows = [{}]
            for key, value in data.items():
                rows = cross_join(rows, flatten_json(value, prev_heading + '.' + key))
        elif isinstance(data, list):
            rows = []
            for i in range(len(data)):
                [rows.append(elem) for elem in flatten_list(flatten_json(data[i], prev_heading))]
        else:
            rows = [{prev_heading[1:]: data}]
        return rows

    return pd.DataFrame(flatten_json(data_in))



with open('{}'.format(input_path2)) as json_file:
        json_data = json.load(json_file)
        df = json_to_dataframe(json_data)
        archive_file=df
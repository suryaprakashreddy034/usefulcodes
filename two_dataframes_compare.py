import re
import sys
#from google.cloud import storage
import pandas as pd
from pandas.io import gbq
import numpy as np

test_Scenario="[TS_Symedical_InitialLoad_009] - To validate the data between the files in GCS archive folder and GCS source file landing for Symedical is matching"
print(test_Scenario)
input_path1="/content/drive/MyDrive/bq-results-20211115-151151-mj2wrsyletgr/first_file - bq-results-20211115-151151-mj2wrsyletgr.csv" #previous query
input_path2="/content/drive/MyDrive/bq-results-20211115-151151-mj2wrsyletgr/second - bq-results-20211115-151151-mj2wrsyletgr.csv" # new Query
data1 = pd.read_csv(input_path1)
input_path1=pd.DataFrame(data1)
data1 = pd.read_csv(input_path2)
input_path2=pd.DataFrame(data1)
common = input_path2.merge(input_path1)
common['result'] = 'MATCHED'

only_first_set=input_path1.loc[~input_path1.set_index(list(input_path1.columns)).index.isin(input_path2.set_index(list(input_path2.columns)).index)]  #dataframe 1 not matched data


only_set_set=input_path2.loc[~input_path2.set_index(list(input_path2.columns)).index.isin(input_path1.set_index(list(input_path1.columns)).index)]  #dataframe 1 not matched data

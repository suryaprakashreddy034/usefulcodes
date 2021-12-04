import json
import pandas as pd
import csv 
from pandas.io.json import json_normalize

df = pd.read_csv('/content/drive/MyDrive/json/input/results-20210809-221634.csv') #csv file with multiple columns of the same name

#function to join columns if column is not null
def sjoin(x): return '|'.join(x[x.notnull()].astype(str))

#function to ignore the suffix on the column e.g. a.1, a.2 will be grouped together
def groupby_field(col):
    parts = col.split('_')
    return '{}'.format(parts[0])

df = df.groupby(groupby_field, axis=1,).apply(lambda x: x.apply(sjoin, axis=1))
df1=pd.DataFrame(df)

print(df1)






import os, zipfile
from datetime import date

import pandas as pd
from pandas.core.indexes.base import Index
import pandas_profiling
from prettytable import PrettyTable
import re as re
import datetime
import numpy as np
import collections


from dateutil.parser import parse
import time, os, fnmatch, shutil  
  
path_file='/content/drive/MyDrive/json/Object - Master Results Dataset 20210817.csv'
split_word=path_file.split('/')
last_split=split_word[-1]
file_name=last_split[:-4]

data = pd.read_csv(path_file)     #input path 
l_x = ['locationfaxnumber']  #pass columns need to find formats
df = pd.DataFrame(data)                             
dimensions_of_table = df.shape
z1 = list(dimensions_of_table)

# print(z)
x_axis1 = z1[0]
y_axis1 = z1[1]
print()
print('ROWS :{}, COLUMNS : {}'.format(x_axis1, y_axis1))
print()

df = pd.DataFrame(df)  # framing of input file data
table_headers = list((df.columns.values))


print(table_headers)
acces_list = []
selected_columns=[]


for i in range(0,y_axis1):

    ind = i
    s4 = []
    df[table_headers[i]] = df[table_headers[i]].apply(str)
    if table_headers[i] in l_x:
        selected_columns.append(table_headers[i])
        z = table_headers.index(table_headers[i])
        if z == i:
            dff = df[table_headers[z]]
            sd = df[table_headers[z]].value_counts()
            s4.append(dff)

    list_values = []

    count_null = 0
    for num in s4:
        for i in num:
            #print(i)
            if i == 'nan':
                count_null=count_null+1
                continue
            else:
                list_values.append(i)
    valid_phone_numbe_list = []
    valid_phone_numbe_list1 = []

    for i in list_values:
        phonenumber = str(i)
        k = '*'
        for ele in phonenumber:
            if ele.isnumeric():
                phonenumber = phonenumber.replace(ele, k)
        valid_phone_numbe_list.append(phonenumber)
    for i in valid_phone_numbe_list:
        phonenumber = str(i)
        k = '#'
        for ele in phonenumber:
            if ele.isalpha():
                phonenumber = phonenumber.replace(ele, k)
        valid_phone_numbe_list1.append(phonenumber)
    counter1 = collections.Counter(valid_phone_numbe_list1)

    a = dict(counter1)
    fd=len(a)
    if fd>0:
        df4 = pd.DataFrame.from_dict(a, orient = 'index')
        acces_list.append(df4)
kl = len(acces_list)
len_arrr=len(selected_columns)

if len_arrr >0:
    save_path = (r"/content/drive/MyDrive/profilingdata/CONGA/format/{}format.xlsx".format(file_name))
    writer = pd.ExcelWriter(save_path)
    print(selected_columns)
    for i in range(0,kl):

      acces_list[i].to_excel(writer,sheet_name='{}'.format(selected_columns[i]))
    writer.save()
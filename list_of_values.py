import os, zipfile
from datetime import date
#from typing import Iterable, final
import pandas as pd
from pandas.core.indexes.base import Index
import pandas_profiling
from prettytable import PrettyTable
import re as re
import datetime
import numpy as np
import collections
import glob


def lov_process(path_file):
  split_word=path_file.split('/')
  last_split=split_word[-1]
  file_name=last_split[:-4]

  data = pd.read_csv(path_file)
  df = pd.DataFrame(data)
  list_1 = (list(df.columns.values))
  result = data.shape
  z = list(result)

  a = z[0]
  b = z[1]

  maa = []
  list_lov_att = []
  selected_columns= []
  for i in range(0, b):
      df[list_1[i]] = df[list_1[i]].apply(str)
      unique_val = df[list_1[i]].nunique(dropna=True)
      total_rows = a
      per = unique_val / total_rows
      perce_1 = per * 100
      percentage = round(perce_1, 2)
      if percentage < 1:
          selected_columns.append(list_1)
          lov = pd.unique(df[list_1[i]])
          list_lov_att.append(list_1[i])
          maa.append(df[list_1[i]])
  dr = pd.DataFrame(maa)
  dr2 = dr.T
  dr3 = pd.DataFrame(dr2)

  list_2 = (list(dr3.columns.values))
  result2 = dr3.shape
  z1 = list(result2)

  a1 = z1[0]
  b1 = z1[1]


  list_lov_att1 = []
  selected_columns1 = []
  xv = []
  acces_list = []
  for i in range(0, b1):
      ind = i

      valid_list1 = []
      valid = []

      dr3[list_2[i]] = dr3[list_2[i]].apply(str)
      if list_2[i] in list_lov_att:
          for i in dr3[list_2[i]]:
              if i == 'nan':
                  n = 'NULL'
                  valid_list1.append(n)
                  continue
              else:
                  valid_list1.append(i)
      counter1 = collections.Counter(valid_list1)
      a=dict(counter1)
      fd=len(a)
      if fd>0:
          df4 = pd.DataFrame.from_dict(a, orient = 'index')
          acces_list.append(df4)
  kl = len(acces_list)
  len_arrr=len(list_lov_att)
  if len_arrr >0:
    save_path = (r"/content/drive/MyDrive/profilingdata/peoplesoft/lov/{}lov.xlsx".format(file_name))
    writer = pd.ExcelWriter(save_path)
    print(list_lov_att)
    for i in range(0,kl):
      acces_list[i].to_excel(writer,sheet_name='{}'.format(list_lov_att[i]))
    writer.save()



files = glob.glob("/content/drive/MyDrive/profilingdata/peoplesoft/input1/*")
print("Total number of files: ", len(files))
print("Showing first 10 files...")
extension_zip = '.csv'
#if path_file.endswith(extension_zip):
for i in range(0,len(files)):
  path_file=files[i]
  if path_file.endswith(extension_zip):
    print(path_file)
    lov_process(path_file)

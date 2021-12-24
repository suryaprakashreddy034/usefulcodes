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
def date_prof(path_file):
  split_word=path_file.split('/')
  last_split=split_word[-1]
  file_name=last_split[:-4]
  data = pd.read_csv(path_file)
  df=pd.DataFrame(data) #framing of input file data
  dimensions_of_table = df.shape
  z1=list(dimensions_of_table)
  #print(z)
  x_axis1=z1[0]
  y_axis1=z1[1]
 
  print(      )
  print('ROWS :{}, COLUMNS : {}'.format(x_axis1,y_axis1))
  print(      )
 
  df_numerics_only1 = df.select_dtypes(include=np.number)
  df_numerics_only=pd.DataFrame(df_numerics_only1)
 
  df_objects1=df.select_dtypes(exclude=np.number)
  df_objects=pd.DataFrame(df_objects1)
 
  list_special=['!','"','#','$','%','&',"'",'(',')','*','+',',','-','.','/',':',';',',','<','=','>','?','@','[',']','^','_','`','{','|','}','~',]
 
 
  def prof_num(df_numerics_only):
      table_header=(list(df_numerics_only.columns.values))   # listing values of table_header
      len_1=len(table_header)  # length of table header
      api=[]
      acces_list=[]
      dimensions_of_table = df_numerics_only.shape    # SHAPING OF CSV FILE TO GET DIMENSIONS
      #output_filename=os.path.basename(path_file) # output file name
      z=list(dimensions_of_table)
      x_axis=z[0]
      y_axis=z[1]
      for i in range(0,y_axis):
          ind=i
          print(i)
          null_value= (df_numerics_only[table_header[i]].isnull().sum()) #5
          value_in_col=df_numerics_only[table_header[i]]
          clean_list=[]
          for k in value_in_col:
              if k != 'nan':
                  clean_list.append(k) 
 
          if len(clean_list)>0:
              df_dup = pd.DataFrame(clean_list)
              duplicated_val=df_dup[0].duplicated().sum()    #6
          else:
              duplicated_val=0
        #print(duplicated_val)
          unique_val=df_numerics_only[table_header[i]].nunique(dropna = True)  #7
          total_rows=x_axis
          attribute_name=table_header[i]  # 0
          list_of_org_val=[]
          s4=[]
          s5=[]
          if ind==ind:
              dff=df_numerics_only[table_header[ind]]
              s4.append(dff)
 
          for num in s4:
              for ik in num:
                  ik=str(ik)
 
                  if ik == 'nan':
                      continue
                  else:
                    kl=float(ik)
                    list_of_org_val.append(kl)
                    jk=int(kl)
 
                    #lk=int(lk)
                    kl=str(jk)
                    le=len(kl)
                    s5.append(le)
 
          special_rows_list=[]
          asas_special=[]
          for i in list_of_org_val:
              row=str(i)
              for internal in row:
                  if internal in list_special:
                      asas_special.append(internal)
                      if row not in special_rows_list:
                          special_rows_list.append(row)
          only_spe_char=[]
          for k in asas_special:
              if k not in only_spe_char:
                  only_spe_char.append(k)
          list_only_spe_char=only_spe_char #14
    
          special_char_count=len(asas_special) #12
        #print(special_char_count)
          count_special_rows=len(special_rows_list)
          count_not_special_rows=total_rows-(count_special_rows + null_value)
          list_of_org_val.sort()
        #print(list_of_org_val)
          len_list_of_org_val=len(list_of_org_val)
 
          if len_list_of_org_val>0:
              min_value=list_of_org_val[0] #1
              max_value=list_of_org_val[-1] #2
    
          else:
              min_value=max_value='null'
 
          ty=len(s5)
          if ty>0:
              s5.sort()
              min_len_value=s5[0]   #3 
            #s5.sort(reverse=True)
              max_len_value=s5[-1] #4
 
          else:
              max_len_value=min_len_value=0
 
          per=unique_val/total_rows
          perce_1=per*100
          percentage=(round(perce_1, 2)) #10
          percentag=str(percentage)+'%'
          if percentage < 1:       
              lov=pd.unique(df_numerics_only[table_header[ind]])  # 13
              len_lov=len(lov)
 
          else:
              lov=[]
              len_lov='HIGHER COUNT OF LIST OF VALUES'
          null_per=(null_value/total_rows)*100
          null_percentage=round(null_per, 2) #9
          null_percentage=str(null_percentage)+'%'
          lov_count=(duplicated_val+unique_val)/total_rows
          lov_per=(lov_count*100)
          lov_percentage=round(lov_per, 4) #11
          lov_percentage=str(lov_percentage)+'%'
 
 
          list_final_atrributes_values= [[attribute_name,min_value,max_value,min_len_value,max_len_value,null_value,duplicated_val,unique_val,total_rows,null_percentage,percentag,lov_percentage,special_char_count,lov,list_only_spe_char]]
          acces_list.append(list_final_atrributes_values)      
    #print(acces_list)
      for i in acces_list:
          ip=i[0]
          api.append(ip)
      len_api=len(api)
 
      table = PrettyTable(['attribute_name','min_value','max_value','min_len_value','max_len_value','null_value','repititive_val','unique_val','total_rows','null_value_percentage','unique_percentage','lov_percentage','special_char_count','list_of_values','list_only_spe_char'])
 
      for i in range(0,len_api):
          table.add_row(api[i])
 
      dew_table1=pd.DataFrame(api,columns =['attribute_name','min_value','max_value','min_len_value','max_len_value','null_value','repititive_val','unique_val','total_rows','null_value_percentage','unique_percentage','lov_percentage','special_char_count','list_of_values','list_only_spe_char'])
    #print(dew_table1)
      return dew_table1
    
  def prof_obj(df_objects):
 
      table_header=(list(df_objects.columns.values))   # listing values of table_header
      len_1=len(table_header)  # length of table header
      api=[]
      acces_list=[]
      dimensions_of_table = df_objects.shape    # SHAPING OF CSV FILE TO GET DIMENSIONS
      z=list(dimensions_of_table)
      x_axis=z[0]
      y_axis=z[1]
      for i in range(0,y_axis): 
          ind=i
          print(i)
          null_value= (df_objects[table_header[i]].isnull().sum()) #5
          df_objects[table_header[i]] = df_objects[table_header[i]].apply(str)
          value_in_col=df_objects[table_header[i]]
          clean_list=[]
          for k in value_in_col:
              if k != 'nan':
                  clean_list.append(k) 
 
          if len(clean_list)>0:
              df_dup = pd.DataFrame(clean_list)
              duplicated_val=df_dup[0].duplicated().sum()    #6
          else:
              duplicated_val=0
        #print(duplicated_val)
          unique_val=df_objects[table_header[i]].nunique(dropna = True)  #7 
        #print(unique_val)
          total_rows=x_axis
          attribute_name=table_header[i]  # 0  
          list_of_org_val=[] 
          s4=[]
          s5=[]
          if ind==ind:
              dff=df_objects[table_header[ind]]
              s4.append(dff)
          for num in s4:
              for i in num:
 
                  if i == 'nan':
 
                      continue
                  else:
                      list_of_org_val.append(i)
                      le=len(i)
                      s5.append(le) 
          special_rows_list=[]
          asas_special=[]
          for i in list_of_org_val:
              row=i
              for internal in row:
                  if internal in list_special:
                      asas_special.append(internal)
                      if row not in special_rows_list:
                          special_rows_list.append(row)
          only_spe_char=[]
          for k in asas_special:
              if k not in only_spe_char:
                  only_spe_char.append(k)
          list_only_spe_char=only_spe_char #14
 
          special_char_count=len(asas_special) #12
 
          count_special_rows=len(special_rows_list)
          count_not_special_rows=total_rows-(count_special_rows + null_value)
          list_of_org_val.sort()
          pi=len(list_of_org_val)
          if pi>0:
              min_value=list_of_org_val[0] #1
              max_value=list_of_org_val[-1] #2           
          else:
              min_value=max_value='null'
 
 
          ty=len(s5)
          if ty>0:
              s5.sort()
              min_len_value=s5[0]   #3 
            #s5.sort(reverse=True)
              max_len_value=s5[-1] #4
 
          else:
              max_len_value=min_len_value=0
 
 
          per=unique_val/total_rows
          perce_1=per*100
          percentage=round(perce_1, 2) #10
          percentag=str(percentage)+'%'
          if percentage < 1:       
              lov=pd.unique(df_objects[table_header[ind]])  # 13
              len_lov=len(lov)
 
          else:
              lov=[]
              len_lov='HIGHER COUNT OF LIST OF VALUES'
          null_per=(null_value/total_rows)*100
          null_percentage=round(null_per, 2) #9
          null_percentage=str(null_percentage)+'%'
          lov_count=(duplicated_val+unique_val)/total_rows
          lov_per=(lov_count*100)
          lov_percentage=round(lov_per, 2) #11
          lov_percentage=str(lov_percentage)+'%'
          list_final_atrributes_values= [[attribute_name,min_value,max_value,min_len_value,max_len_value,null_value,duplicated_val,unique_val,total_rows,null_percentage,percentag,lov_percentage,special_char_count,lov,list_only_spe_char]]
          acces_list.append(list_final_atrributes_values)
    #print(acces_list)
      for i in acces_list:
          ip=i[0]
          api.append(ip)
      len_api=len(api)
 
      table = PrettyTable(['attribute_name','min_value','max_value','min_len_value','max_len_value','null_value','repititive_val','unique_val','total_rows','null_value_percentage','unique_percentage','lov_percentage','special_char_count','list_of_values','list_only_spe_char'])
 
      for i in range(0,len_api):
          table.add_row(api[i])
    #print(table)
      dew_table2=pd.DataFrame(api,columns =['attribute_name','min_value','max_value','min_len_value','max_len_value','null_value','repititive_val','unique_val','total_rows','null_value_percentage','unique_percentage','lov_percentage','special_char_count','list_of_values','list_only_spe_char'])
    #print(dew_table2)
      return dew_table2
 
 
 
  tab1=prof_num(df_numerics_only)
  tab2=prof_obj(df_objects)
 
 
 
  frames = [tab1,tab2]
  result = pd.concat(frames,ignore_index=True)
  print(result)
  with open('/content/drive/MyDrive/profilingdata/peoplesoft/output/{}.csv'.format(file_name),'w') as f:
    result.to_csv(f)
  with open('/content/drive/MyDrive/profilingdata/peoplesoft/output2/{}.csv'.format(file_name),'w') as f:
    result.to_csv(f)
 
 
 
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
    date_prof(path_file)
    lov_process(path_file)
 
 

import pandas as pd


data = pd.read_csv(r"C:/Users/sprakashreddychin/Desktop/sqltesting/firsttable.csv",encoding='latin1')
df1=pd.DataFrame(data)
data = pd.read_csv(r"C:/Users/sprakashreddychin/Desktop/sqltesting/secondtable.csv",encoding='latin1')
df2=pd.DataFrame(data)
df5=df2

df1=df1.set_index("rollno")
df2=df2.set_index("rollno")

df3=pd.concat([df1,df2],sort=False)
df3a=df3.stack().groupby(level=[0,1]).unique().unstack(1).copy()
idx=df3.stack().groupby(level=[0,1]).nunique()
df3a.loc[idx.mask(idx<=1).dropna().index.get_level_values(0),'status']="record_modified"
data_validation=pd.DataFrame(df3a)
options = ["record_modified"]
# selecting rows based on condition
rslt_df = data_validation[data_validation['status'].isin(options)]
data_validation=pd.DataFrame(rslt_df)
data_validation.reset_index(level=0, inplace=True)
modified_ids=list(data_validation["rollno"])
rslt_df = df5[df5['rollno'].isin(modified_ids)]
rslt_df['result'] = 'record_modified'
print(rslt_df)

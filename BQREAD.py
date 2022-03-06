from google.cloud import bigquery
from google.oauth2 import service_account
import pandas as pd
credentials = service_account.Credentials.from_service_account_file("C:/Users/surya/Downloads/aams-sbx-eb22dc8165ca.json")
project_id = 'aams-sbx'
client = bigquery.Client(credentials= credentials,project=project_id)
QUERY="""SELECT distinct(file_names) FROM `aams-sbx.beer.sedfr`"""
query_job = client.query(QUERY)
df = query_job.to_dataframe()
print(list(df["file_names"]))



    

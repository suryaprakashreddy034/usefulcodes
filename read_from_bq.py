import re
import sys
from google.cloud import storage
import pandas as pd
from pandas.io import gbq
from datetime import datetime



input_path="""select * from table """  

project_id='project_id'

current_data_query=input_path
current_data=gbq.read_gbq(current_data_query,project_id)

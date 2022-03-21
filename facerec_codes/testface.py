import csv
import os.path
from os import path
from csv import writer
from genericpath import exists
header = ['name', 'area', 'country_code2', 'country_code3']
data = [
    ['Albanwwia', 28748, 'AL', 'ALB']
]

with open('/home/surya/Desktop/facerec_codes/attendence/countries.csv', 'a+', encoding='UTF8', newline='\n') as f:

    if str(path.exists('/home/surya/Desktop/facerec_codes/attendence/countries.csv')) == "False":

        writer = csv.writer(f)

    # write the header
        writer.writerow(header)

    # write multiple rows
        writer.writerows(data)
    else:
        writer = csv.writer(f)
    # write multiple rows
        writer.writerows(data)


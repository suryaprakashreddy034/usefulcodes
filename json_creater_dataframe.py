import json
import pandas as pd
import csv 
from pandas.io.json import json_normalize

df = pd.read_csv('/content/drive/MyDrive/json/input/results-20210809-093804.csv') #csv file with multiple columns of the same name

#function to join columns if column is not null
def sjoin(x): return '||'.join(x[x.notnull()].astype(str))

#function to ignore the suffix on the column e.g. a.1, a.2 will be grouped together
def groupby_field(col):
    parts = col.split('_')
    return '{}'.format(parts[0])

df = df.groupby(groupby_field, axis=1,).apply(lambda x: x.apply(sjoin, axis=1))
df1=pd.DataFrame(df)

main=df1.to_dict('records')
print(main)

output = {'persons': []}
for person in main:
  main=dict(person)
  output['persons'].append(
      {
    "type": "configuration/entityTypes/HCP",
    "attributes": {
      "ManagedIdentifiers": [
        {
          "value": {
            "ManagedIdentifierType": [
              {
                "value": "NPI"
              }
            ],
            " Managed IdentifierValue": [
              {
                "value": "302"
              }
            ],
            "State": [
              {
                "value": "USA"
              }
            ],
            "IssueDate": [
              {
                "value": "02-08-2021"
              }
            ]
          }
        }
        
      ],
      "Phone": [
        {
          "value": {
            "Type": [
              {
                "value": "Home"
              }
            ],
            "Number": [
              {
                "value": "91256009"
              }
            ]
          }
        }
      ],
      "FirstName": [
        {
          "value": "Linda"
        }
      ],
      "LastName": [
        {
          "value": "Smith"
        }
      ],
      "Prefix": [
        {
          "value": "Dr"
        }
      ],
      "AcademicDegree": [
        {
          "value": main['AcademicDegree']
        }
      ],
	  "Gender": [
        {
          "value": "M"
        }
      ],
	    "Email": [
        {
          "value": {
            "Type": [
              {
                "value": "Work"
              }
            ],
            "Number": [
              {
                "value": "Linda@gmail.com"
              }
            ]
          }
        }
      ]
	  },
    "crosswalks": [
      {
        "type": "configuration/sources/MD Staff",
        "value": "MDSTAFF234578"
      }
    ]
  }
      


  )

output_json = json.dumps(output,indent=3)
print(output_json)


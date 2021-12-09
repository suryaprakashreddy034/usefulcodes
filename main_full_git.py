import json
import requests
from pandas.io.json import json_normalize
import pandas
import numpy as np
from copy import deepcopy

def cross_join(left, right):
    new_rows = [] if right else left
    for left_row in left:
        for right_row in right:
            temp_row = deepcopy(left_row)
            for key, value in right_row.items():
                temp_row[key] = value
            new_rows.append(deepcopy(temp_row))
    return new_rows


def flatten_list(data):
    for elem in data:
        if isinstance(elem, list):
            yield from flatten_list(elem)
        else:
            yield elem


def json_to_dataframe(data_in):
    def flatten_json(data, prev_heading=''):
        if isinstance(data, dict):
            rows = [{}]
            for key, value in data.items():
                rows = cross_join(rows, flatten_json(value, prev_heading + '.' + key))
        elif isinstance(data, list):
            rows = []
            for i in range(len(data)):
                [rows.append(elem) for elem in flatten_list(flatten_json(data[i], prev_heading))]
        else:
            rows = [{prev_heading[1:]: data}]
        return rows

    return pandas.DataFrame(flatten_json(data_in))

GITHUB_USERNAME="suryaprakashreddy034"
GITHUB_TOKEN="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"

github_api = "https://api.github.com"
gh_session = requests.Session()
gh_session.auth = (GITHUB_USERNAME,GITHUB_TOKEN)
url = github_api + '/repos/suryaprakashreddy034/gcp_codes/pulls/1'
commits = gh_session.get(url = url)
commits_json = commits.json()
'''
#print(json.dumps(commits_json, indent=4))
URL="https://api.github.com/repos/suryaprakashreddy034/gcp_codes/issues/2/comments"
r = requests.get(url = URL)

# extracting data in json format
'''
data = commits.text
json_data = json.loads(data)
df = json_to_dataframe(json_data)


URL_issues=df["_links.comments.href"].iloc[0]
URL_pulls=df["_links.review_comments.href"].iloc[0]
#print(json.dumps(commits_json, indent=4))
#URL="https://api.github.com/repos/suryaprakashreddy034/gcp_codes/issues/2/comments"
r = requests.get(url = URL_issues)
data = r.text
json_data = json.loads(data)
df = json_to_dataframe(json_data)
print(df)
# extracting data in json format

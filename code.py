import json
import requests
from pandas.io.json import json_normalize
import pandas as pd
import numpy as np


GITHUB_USERNAME="suryaprakashreddy034"
GITHUB_TOKEN="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"

github_api = "https://api.github.com"
gh_session = requests.Session()
gh_session.auth = (GITHUB_USERNAME,GITHUB_TOKEN)
url = github_api + '/repos/apache/spark/commits'
commits = gh_session.get(url = url)
commits_json = commits.json()
print(commits_json)

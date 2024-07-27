# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json
import os

url = "https://aashrithadodda79.atlassian.net/rest/api/3/project"

token = os.getenv("API_TOKEN")

auth = HTTPBasicAuth("aashritha.dodda79@gmail.com", token)

headers = {
  "Accept": "application/json"
}

response = requests.request(
   "GET",
   url,
   headers=headers,
   auth=auth
)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))

# output = json.loads(response.text)

# name = output[0]["name"]

# print(name)



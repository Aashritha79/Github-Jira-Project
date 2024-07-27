import requests
from requests.auth import HTTPBasicAuth
import json
import os

url = "https://aashrithadodda79.atlassian.net/rest/api/3/issue"

token = os.getenv("API_TOKEN")

auth = HTTPBasicAuth("aashritha.dodda79@gmail.com", token)

headers = {
  "Accept": "application/json",
  "Content-Type": "application/json"
}

payload = json.dumps( {
  "fields": {
    "description": {
      "content": [
        {
          "content": [
            {
              "text": "My first jira ticket",
              "type": "text"
            }
          ],
          "type": "paragraph"
        }
      ],
      "type": "doc",
      "version": 1
    },
    "project": {
      "key": "GJP"
    },
    "issuetype": {
      "id": "10003"
    },
    "summary": "Second JIRA Ticket",
  },
  "update": {}
} )

response = requests.request(
   "POST",
   url,
   data=payload,
   headers=headers,
   auth=auth
)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))

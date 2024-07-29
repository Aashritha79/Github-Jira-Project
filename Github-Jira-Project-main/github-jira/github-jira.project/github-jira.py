import requests
from requests.auth import HTTPBasicAuth
import json
import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/createJira', methods=['POST'])
def createJira():
    url = "https://aashrithadodda79.atlassian.net/rest/api/3/issue"
    token = os.getenv(API_TOKEN")
    
    auth = HTTPBasicAuth("aashritha.dodda79@gmail.com", token)
    
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

    payload = {
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
    }

    webhook = request.json

    response = None

    if webhook.get('comment') and webhook['comment'].get('body') == "/jira":
        response = requests.post(
            url,
            data=json.dumps(payload),
            headers=headers,
            auth=auth
        )
        return json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": "))
    else:
        return json.dumps({"status": "no action taken", "message": "Comment does not include /jira"}, sort_keys=True, indent=4, separators=(",", ": "))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

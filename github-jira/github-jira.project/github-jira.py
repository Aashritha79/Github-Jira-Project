# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json
from flask import Flask

app = Flask(__name__)

@app.route('/createJira', methods=['POST'])
def createJira():

    url = "https://aashrithadodda79.atlassian.net/rest/api/3/issue"

    API_TOKEN="ATATT3xFfGF0qD200gqlwpSovi27yjdvnLB65dhUz3M4hVsmKprcuCev1N00b96C0sgG237zVK2-GTMg3QwOwVMslQSvHAuPzlqiFsy-zs63G8njMJA4ZcdMy9zKCP7xjiwEFYKPhl3LH_238hRU8KTltrOstcKRqZ7DdVfBZmWtrHi8HtGSaYc=C4DB99E5"

    auth = HTTPBasicAuth("aashritha.dodda79@gmail.com", API_TOKEN)

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
                            "text": "Order entry fails when selecting supplier.",
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
        "summary": "Main order flow broken",
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

    return json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": "))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
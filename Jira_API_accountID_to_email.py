import json

import requests

url = "https://ipinfo.io/what-is-my-ip1452-2152"
url1 = "https://ipinfo.io/geo"

user = ""
apitoken = ""

headers = {
    "Accept": "application/json",
    "Content-Type": "application/json",
}

issue_dict = {
    "fields": {
        "project": {"key": "IIP"},
        "summary": "Create Ticket Via API",
        "description": "Create Ticket Via API",
        "issuetype": {"name": "Issue"},
        "priority": {"name": "Priority"}
    }

}
payload = json.dumps(issue_dict)

response = requests.get(url,auth=(user,apitoken),headers=headers)

mydata = response.json()
print(mydata['emailAddress'])


import json
import requests

# 1. Fill in Your Jira Details
JIRA_URL = "https://YOUR-DOMAIN.atlassian.net"  # **BLANK 1: Your Jira Base URL**
JIRA_ISSUE_ENDPOINT = f"{JIRA_URL}/rest/api/3/issue"  # Correct endpoint for creating issues

# **BLANK 2: Your Jira Username (usually email)**
user = "YOUR_JIRA_EMAIL"
# **BLANK 3: Your Jira API Token (NOT your password)**
apitoken = "YOUR_JIRA_API_TOKEN"

headers = {
    "Accept": "application/json",
    "Content-Type": "application/json",
}

# 2. Define the Issue Payload
issue_dict = {
    "fields": {
        # **BLANK 4: Your Project Key (e.g., 'SCRUM', 'HELP')**
        "project": {"key": "IIP"},
        "summary": "Create Ticket Via API",
        "description": "This issue was created successfully using a Python script via the REST API.",
        # Fix 5: Comma missing after issuetype
        # **BLANK 5: Your Issue Type Name (e.g., 'Bug', 'Story', 'Task')**
        "issuetype": {"name": "Task"},
        # Fix 6: Priority should be a separate item if needed
        # **BLANK 6: Your Priority Name (e.g., 'High', 'Medium', 'Low')**
        "priority": {"name": "High"}
    }
}
payload = json.dumps(issue_dict)

try:
    # 3. Perform the POST request to create the issue
    # We use POST for creation and the JIRA_ISSUE_ENDPOINT
    response = requests.post(
        JIRA_ISSUE_ENDPOINT,
        auth=(user, apitoken),
        headers=headers,
        data=payload
    )

    # 4. Handle the response
    response.raise_for_status()  # Raise an exception for bad status codes (4xx or 5xx)

    mydata = response.json()
    print("✅ Jira Issue Creation Successful!")
    # Fix 7: Print the created issue key and URL, which Jira returns upon success
    print(f"New Issue Key: {mydata.get('key')}")
    print(f"View Issue Here: {JIRA_URL}/browse/{mydata.get('key')}")

except requests.exceptions.RequestException as e:
    print(f"❌ Jira API Request Failed.")
    print(f"Error Details: {e}")
    if 'response' in locals() and hasattr(response, 'text'):
        print(f"Server Response: {response.text}")
import json
import requests

# Fix 1: Use a valid public IP information URL
# The original print line 'mydata['emailAddress']' is invalid for this service,
# so we will print the IP address instead.
url = "https://api.ipify.org?format=json"  # Gets the public IP in JSON format

# Fix 2: Remove unnecessary authentication variables/headers for a simple GET request
# Jira credentials (user, apitoken) and headers are not needed here.
# user = ""
# apitoken = ""
# headers = {} # Not needed for this simple request

# The issue_dict payload for Jira is not used in this script.

try:
    # Fix 3: Perform the GET request without authentication
    response = requests.get(url)

    # Check for a successful response code (e.g., 200)
    response.raise_for_status()

    mydata = response.json()

    # Fix 4: Print a valid key from the response data (ipify returns 'ip')
    print(f"✅ Successful API Request")
    print(f"My Public IP Address is: {mydata['ip']}")

except requests.exceptions.RequestException as e:
    print(f"❌ An error occurred during the request: {e}")
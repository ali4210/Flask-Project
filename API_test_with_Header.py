import requests
url = "https://ipinfo.io/what-is-my-ip1452-2152"
url1 = "https://ipinfo.io/geo"


headers = {
    "Accept": "application/json",
    "Content-Type": "application/json",
}


response = requests.get(url)

my_status_code = response.status_code
my_headers = response.headers
print(my_status_code)
print(my_headers)

if my_status_code == 200:
    print("Status:",my_status_code,"Headers:",my_headers, "response:",response.json())
else:
    print("ERROR \n:",my_status_code,"Headers:",my_headers, "response:",response.json())

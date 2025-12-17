import requests
url = "https://ipinfo.io/what-is-my-ip"
url1 = "https://ipinfo.io/geo"

response = requests.get(url)
print(response.status_code)
print(response.text)

mydata = response.json()
print(mydata)

for key,value in mydata.items():
    print(key,":",value)

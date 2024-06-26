import requests

response = requests.get("http://api.open-notify.org/astros.json")
json = response.json()

print(response)  # <Response [200]>
print(json)  # daje cały json bez codu

for person in json["people"]:
    print(person["name"])

import json
import requests

url = "https://api.opencovid.ca"
response = requests.get(url)

data = json.loads(response.text)

for key in data["summary"][0]:
    if isinstance(data["summary"][0][key], float):
        print("{}: {:,.0f}" .format(key, data["summary"][0][key]))
    else:
        print(key + ":", data["summary"][0][key])
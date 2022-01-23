import json
import requests

url = "https://api.opencovid.ca/other?stat=prov"
response = requests.get(url)

data = json.loads(response.text)

for province in data["prov"]:
    if province["pop"] != "NULL":
        print("{}: {:,.0f}" .format(province["province"], province["pop"]))
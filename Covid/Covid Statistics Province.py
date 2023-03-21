import json
import requests
import pandas as pd
import matplotlib.pyplot as plt

url = "https://api.opencovid.ca/other?stat=prov"
response = requests.get(url)
data = json.loads(response.text)
# Dumps - Converts dictionary into string (dumps the json into a string)
    # Dumps - Dumps the json into a string
    # Dump - Write json into a file
    # Loads - Converts string to json
    # Load - Load json-data file to json

data["prov"].pop() # pop the NULL
df = pd.read_json(json.dumps(data["prov"]))
# print(df)
df.plot.bar(
    x = "province",
    y = "pop"
)
plt.show()

# for province in data["prov"]:
#     if province["pop"] != "NULL":
#         print("{}: {:,.0f}" .format(province["province"], province["pop"]))
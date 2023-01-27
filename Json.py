import json
import requests

with open("db.json") as json_file:
    data = json.load(json_file)
    for datas in data['Employee']:
        # print(datas['name'])
        # print(datas['id'])
        # print(datas)

        jsonconvert = json.dumps(datas)
        print(jsonconvert)

url = "https://api.punkapi.com/v2/beers/random"

res = requests.get(url)
item=json.loads(res.text)

print(item[0]['name'])



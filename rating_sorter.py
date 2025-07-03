import json
from pprint import pprint

with open("students.json") as jsonfile:
    data = json.load(jsonfile)
    
    sortlangan = sorted(data,key=lambda x:int(x["score"]),reverse=True)

with open("rating.json","w") as jsonfile:
    json.dump(sortlangan,jsonfile,indent=4)
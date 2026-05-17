import json

with open("settings.json") as f:
    data = json.load(f)

print(data)

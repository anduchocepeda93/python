
import json

with open("config.json") as f:
    data = json.load(f)

if data.get("environment") == "prod":
    print("⚠️ Running in production")

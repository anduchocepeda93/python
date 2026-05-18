import requests
import time

for i in range(3):
    try:
        r = requests.get("https://api.example.com")
        if r.status_code == 200:
            print("Success")
            break
    except:
        time.sleep(2)
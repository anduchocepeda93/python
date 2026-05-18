
import requests

url = "https://api.github.com/repos/python/cpython"

try:
    response = requests.get(url, timeout=5)
    response.raise_for_status()
    data = response.json()

    print("Repo:", data["name"])
    print("Stars:", data["stargazers_count"])

except requests.exceptions.RequestException as e:
    print("API error:", e)

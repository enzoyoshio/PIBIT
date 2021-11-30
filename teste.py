import json
import urllib.request
import requests
import hashlib

user_data = ""

# essa parte eu posso fazer dinamico para pegar qualquer user
user_URL = "https://codeforces.com/api/user.info?handles=" + "smeke"

results = requests.get("https://codeforces.com/api/user.info", params = {"handles" : "EYZ"})
test = json.dumps(results.json(), sort_keys=True, indent=4)
print(test)


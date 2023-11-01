import requests

reponsenes = requests.get(url="http://api.open-notify.org/iss-now.json")

print(reponsenes)

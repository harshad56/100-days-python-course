import requests

reponsenes = requests.get(url="http://api.open-notify.org/iss-now.json")
reponsenes.raise_for_status()

data = reponsenes.json()

longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]

is_position = (longitude, latitude)

print(is_position)

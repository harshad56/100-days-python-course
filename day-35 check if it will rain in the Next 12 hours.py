import requests

end_points = "https://api.openweathermap.org/data/2.5/weather"
api_key = "a0ec14516b920ad5ded92db552f2281b"

weather_parms = {
    "lat": 19.075983,
    "lon": 72.877655,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(end_points, params=weather_parms)
response.raise_for_status()
weather_data = response.json()

weather_slice = weather_data["wind"]
for data in weather_slice:
    print(data)

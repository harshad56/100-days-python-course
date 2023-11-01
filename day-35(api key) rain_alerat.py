import requests

end_points = "https://api.openweathermap.org/data/2.5/weather"
api_key = "a0ec14516b920ad5ded92db552f2281b"

weather_parms = {
    "lat": 19.218330,
    "lon": 72.978088,
    "appid": api_key,
}

response = requests.get(end_points, params=weather_parms)
print(response.json())

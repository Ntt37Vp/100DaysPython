import requests

# Constants
api_url = "https://api.openweathermap.org/data/2.5/forecast"
parameters = {
    "lat": 9.306840,
    "lon": 123.305450,
    "appid": "934276031be400eb89221d212fc2e067"
}

response = requests.get(api_url, params=parameters)
response.raise_for_status()
weather_data = response.json()
for i in range(0, 8):
    print(weather_data["list"][i]["weather"][0]["id"])

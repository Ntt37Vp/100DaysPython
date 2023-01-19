import requests
import constants


response = requests.get(constants.api_url, params=constants.parameters)
response.raise_for_status()
weather_data = response.json()
for i in range(0, 8):
    print(weather_data["list"][i]["weather"][0]["id"])

# ISS Locator
import requests

iss_url = "http://api.open-notify.org/iss-now.json"

response = requests.get(url=iss_url)
# print(response)

# Getting the JSON data from api
data = response.json()


# Getting the specific data
longitude = response.json()["iss_position"]["longitude"]
latitude = response.json()["iss_position"]["latitude"]
iss_coordinate = (longitude, latitude)
print(iss_coordinate)

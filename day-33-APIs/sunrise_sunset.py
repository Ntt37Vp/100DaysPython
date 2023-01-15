# Sunrise Sunset Time
import requests
from datetime import datetime

# Constants
api_url = "https://api.sunrise-sunset.org/json"
parameters = {
    "lat": 10.315699,
    "lng": 123.885437,
    "formatted": 0
}


response = requests.get(api_url, params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]
# print(f"Sunrise: {sunrise} Sunset: {sunset}")

# Extracting the Hour
sunrise_hour = sunrise.split("T")[1].split(":")[0]
sunset_hour = sunset.split("T")[1].split(":")[0]
print(sunrise_hour)
print(sunset_hour)

time_now = datetime.now()
print(time_now.hour)

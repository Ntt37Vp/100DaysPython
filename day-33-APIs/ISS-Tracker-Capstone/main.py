import requests
from datetime import datetime

# Constants
MY_LAT = 10.315699
MY_LONG = 123.885437
MARGIN_ERROR = 5.0  # Position is within +5 or -5 degrees of the ISS position


# ISS locator
def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if abs(iss_latitude - MY_LAT) <= MARGIN_ERROR or abs(iss_longitude - MY_LONG) <= MARGIN_ERROR and is_dark:
        pass

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

# Sunrise Sunset of Location
response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

# Checking Time
is_dark = False
time_now = datetime.now()
hour_now = time_now.hour
if sunset < hour_now < sunrise:
    is_dark = True

# Test values

print(hour_now)
print(sunrise)
print(sunset)
print(is_dark)





import requests
from datetime import datetime
import smtplib
import time

# Constants
MY_LAT = 10.315699
MY_LONG = 123.885437
MARGIN_ERROR = 5.0  # Position is within +5 or -5 degrees of the ISS position
MY_USER = "nortepedro294@gmail.com"
MY_PASS = "yzvtcxnhrbyjvfkj"
MY_RECIPIENT = "dr.pedronorte@yahoo.com"


# ISS locator
def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if abs(iss_latitude - MY_LAT) <= MARGIN_ERROR or abs(iss_longitude - MY_LONG) <= MARGIN_ERROR:
        return True


# Checking Night
def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour
    if time_now >= sunset or time_now <= sunrise:
        return True


while True:
    time.sleep(900)
    if is_iss_overhead() and is_night():
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(user=MY_USER, password=MY_PASS)
        connection.sendmail(
            from_addr=MY_USER,
            to_addrs=MY_RECIPIENT,
            msg="Subject:ISS Alert!\n\nHey Look Up, ISS is overhead!"
        )

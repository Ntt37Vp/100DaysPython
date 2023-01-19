import requests
from datetime import datetime
import smtplib
import time
import constants



# ISS locator
def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if abs(iss_latitude - constants.MY_LAT) <= constants.MARGIN_ERROR or abs(iss_longitude - constants.MY_LONG) <= constants.MARGIN_ERROR:
        return True


# Checking Night
def is_night():
    parameters = {
        "lat": constants.MY_LAT,
        "lng": constants.MY_LONG,
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
        connection.login(user=constants.MY_USER, password=constants.MY_PASS)
        connection.sendmail(
            from_addr=constants.MY_USER,
            to_addrs=constants.MY_RECIPIENT,
            msg="Subject:ISS Alert!\n\nHey Look Up, ISS is overhead!"
        )

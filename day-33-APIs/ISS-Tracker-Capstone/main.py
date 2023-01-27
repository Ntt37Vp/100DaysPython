import requests
from datetime import datetime
import time
import os
import constants
# import smtplib


MARGIN_ERROR = 5
TG_ENDPOINT = "https://api.telegram.org/bot"
ISS_ENDPOINT = "http://api.open-notify.org/iss-now.json"
MESSAGE = "***ISS ALERT 🛰️ 🚀 🔭***\nLook Up,DK!\nISS is overhead!"


# ISS locator
def is_iss_overhead():
    response = requests.get(ISS_ENDPOINT)
    response.raise_for_status()
    data = response.json()
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if abs(iss_latitude - constants.MY_LAT) <= MARGIN_ERROR or \
            abs(iss_longitude - constants.MY_LONG) <= MARGIN_ERROR:
        return True


# Checking Night
def is_night():
    parameters = {
        "lat": os.environ.get("MY_LAT"),
        "lng": os.environ.get("MY_LONG"),
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


# Send TG
def telegram_sendtext(bot_message):
    bot_token = constants.tg_token
    bot_chatID = constants.tg_bot_chatID
    send_text = "https://api.telegram.org/bot" + bot_token + "/sendMessage?chat_id=" + bot_chatID +\
                "&parse_mode=Markdown&text=" + bot_message
    tele_response = requests.get(send_text)
    return tele_response.json()


while True:
    time.sleep(300)
    if is_iss_overhead() and is_night():
        telegram_sendtext(MESSAGE)

# TEST
# telegram_sendtext(MESSAGE)

# Send Email
# while True:
#     time.sleep(900)
#     if is_iss_overhead() and is_night():
#         connection = smtplib.SMTP("smtp.gmail.com")
#         connection.starttls()
#         connection.login(user=constants.MY_USER, password=constants.MY_PASS)
#         connection.sendmail(
#             from_addr=constants.MY_USER,
#             to_addrs=constants.MY_RECIPIENT,
#             msg="Subject:ISS Alert!\n\nHey Look Up, ISS is overhead!"
#         )

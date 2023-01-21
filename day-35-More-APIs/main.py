# OpenWeather 5 Day 3-Hour Forecast data
import os
import requests
import constants


response = requests.get(constants.api_url, params=constants.parameters)
response.raise_for_status()
weather_data = response.json()

will_rain = False


# Telegram bot
def telegram_sendtext(bot_message):
    bot_token = os.environ.get("BOT_TOKEN")
    bot_chatID = os.environ.get("BOT_CHATID")
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    tele_response = requests.get(send_text)
    return tele_response.json()


# Using FOR loop (loop thru 24 hours forecast or 8 3-hour interval)
for i in range(0, 8):
    code = weather_data["list"][i]["weather"][0]["id"]
    weather_description = weather_data["list"][i]["weather"][0]["description"]
    date = weather_data["list"][i]["dt_txt"]
    temp = weather_data["list"][i]["main"]["temp"]
    weather_forecast = f"Weather Forecast as of {date} :\n Temp:{temp}C {code}-{weather_description}"
    telegram_sendtext(weather_forecast)


# OR using slicing method (Angela approach)
# weather_slice = weather_data["list"][:9]
#
# for interval in weather_slice:
#     condition_code = interval["weather"][0]["id"]
#     if int(condition_code) < 700:
#         will_rain = True
#
# if will_rain:
#     telegram_sendtext("Bring an Umbrella.")

import requests
import os
import constants


# Constants
TARGET_MARGIN = 4.0
STOCK = "TSLA"
COMPANY_NAME = "Tesla"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
TG_ENDPOINT = "https://api.telegram.org/bot"
STOCK_PARAM = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK,
    "apikey": os.environ.get("ALPHA_VANTAGE_API"),
}
NEWS_PARAM = {
    "apiKey": os.environ.get("NEWS_API"),
    "searchIn": "title,description",
    "q": COMPANY_NAME,
}

# Fetch Stock Prices
response = requests.get(STOCK_ENDPOINT, params=STOCK_PARAM)
response.raise_for_status()
stock_data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in stock_data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = float(yesterday_data["4. close"])
before_yesterday_data = data_list[1]
before_yesterday_closing = float(before_yesterday_data["4. close"])
delta = abs(yesterday_closing_price - before_yesterday_closing)
delta_percent = (delta / before_yesterday_closing) * 100


def telegram_sendtext(bot_message):
    bot_token = constants.tg_token
    bot_chatID = constants.tg_bot_chatID
    send_text = "https://api.telegram.org/bot" + bot_token + "/sendMessage?chat_id=" + bot_chatID + "&parse_mode=Markdown&text=" + bot_message
    tele_response = requests.get(send_text)
    return tele_response.json()


if delta_percent > TARGET_MARGIN:
    response_getnews = requests.get(NEWS_ENDPOINT, params=NEWS_PARAM)
    response_getnews.raise_for_status()
    top_3_articles = response_getnews.json()["articles"][:3]

    formatted = [f"Headline: {article['title']}\nBrief:{article['description']}" for article in top_3_articles]
    for article in formatted:
        telegram_sendtext(article)

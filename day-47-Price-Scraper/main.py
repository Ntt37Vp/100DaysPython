import requests
from bs4 import BeautifulSoup

product_url = "https://www.amazon.com/Duo-Evo-Plus-esterilizadora-vaporizador/dp/B07W55DDFB/ref=sr_1_4?qid=1597660904"
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/110.0",
    "Accept-Language": "en-US,en;q=0.5"
}

response = requests.get(product_url, headers=header)

soup = BeautifulSoup(response.text, 'html.parser')
# print(soup.prettify())

price = soup.select_one(".a-price span").getText()
price_without_currency = price.split("$")[1]
price_float = float(price_without_currency)
print(price_float)
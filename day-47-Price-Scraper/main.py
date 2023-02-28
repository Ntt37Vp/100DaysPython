import requests, smtplib
from bs4 import BeautifulSoup


# Constants
BUY_PRICE = 100.0
SMTP_ADDRESS = "smtp.gmail.com"
MY_EMAIL = "sender@gmail.com"
MY_PASS = "pass"
RECIPIENT = "recipient@yahoo.com"
product_url = "https://www.amazon.com/dp/B09W28YNHJ/ref=syn_sd_onsite_desktop_0?ie=UTF8&pd_rd_plhdr=t&th=1"
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/110.0",
    "Accept-Language": "en-US,en;q=0.5"
}

response = requests.get(product_url, headers=header)
soup = BeautifulSoup(response.text, 'html.parser')
# print(soup.prettify())

price = soup.find(name="span", class_="a-offscreen").get_text().split("$")[1]
price_float = float(price)
print(price_float)

# Email Notif
title = soup.find(id="productTitle").get_text().strip()
if price_float < BUY_PRICE:
    message = f"{title} is now {price}"

    with smtplib.SMTP(SMTP_ADDRESS, port=587) as connection:
        connection.starttls()
        result = connection.login(MY_EMAIL, MY_PASS)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=RECIPIENT,
            msg=f"Subject:AMZN Price Alert!\n\n{message}\n{product_url}"
        )

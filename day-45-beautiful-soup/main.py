from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")
yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, "html.parser")

headline_tags = soup.find(class_="titleline")
article_text = headline_tags.get_text()
article_link = headline_tags.get("href")
article_votes = soup.find(name="span", class_="score").get_text()
print(article_text)
print(article_link)
print(article_votes)

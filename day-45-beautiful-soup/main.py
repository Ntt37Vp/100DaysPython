from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")
soup = BeautifulSoup(response.text, "html.parser")

article_tags = soup.find_all(class_="titleline")

article_texts = []
article_links = []
for article in article_tags:
    text = article_tags.getText()
    article_texts.append(text)
    link = article_tags.get("href")
    article_links.append(link)

article_votes = soup.find_all(name="span", class_="score").getText()

print(article_texts)
print(article_links)
print(article_votes)

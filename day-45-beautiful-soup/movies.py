import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# create soup
response = requests.get(URL)
soup = BeautifulSoup(response.text, 'html.parser')
print(soup)

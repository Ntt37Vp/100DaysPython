from selenium import webdriver
from selenium.webdriver.chrome.service import Service

target_url = "https://www.python.org/"

service = Service('C:/Users/DK/Documents/DEV/chromedriver.exe')
driver = webdriver.Chrome(service=service)

# Scrape
driver.get(target_url)

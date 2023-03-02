from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

target_url = "https://www.python.org/"
service = Service('C:/Users/DK/Documents/DEV/chromedriver.exe')

driver = webdriver.Chrome(service=service, options=chrome_options)

# Scrape
driver.maximize_window()
driver.get(target_url)
dates = driver.find_elements(By.CSS_SELECTOR, ".event-widget time")
events = driver.find_elements(By.CSS_SELECTOR, ".event-widget li a")

# for date in dates:
#     print(date.text)
# for event in events:
#     print(event.text)

all_events = {}
for n in range(len(events)):
    all_events[n] = {
        "time": dates[n].text,
        "name": events[n].text,
    }
print(all_events)

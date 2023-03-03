from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

target_url = "https://en.wikipedia.org/wiki/Main_Page"
service = Service("/home/dk/Documents/chromedriver")
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.maximize_window()
driver.get(target_url)
article_count = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
# print(article_count.text)
# article_count.click()

# Finding element by link text
# create_account_link = driver.find_element(By.LINK_TEXT, "Create account")
# create_account_link.click()

# Finding a search bar
search_bar = driver.find_element(By.NAME, "search")
search_bar.send_keys("Python")
search_bar.send_keys(Keys.ENTER)

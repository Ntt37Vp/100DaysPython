from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time


# Keep browser up
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# Constants
target = "http://orteil.dashnet.org/experiments/cookie/"
service = Service("/home/dk/Documents/chromedriver")
timeout = time.time() + 5
five_min = time.time() + 60 * 5

# Driver
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.get(target)

# Gets cookie
cookie = driver.find_element(By.ID, "cookie")
while True:
    cookie.click()

    if time.time() > timeout:
        pass

    # Add another 5 sec for next check
    timeout = time.time() + 5

    # After 5 min, stop the bot and check cookie per sec score
    if time.time() > five_min:
        cookie_cps = driver.find_element(By.ID, "cps").text
        print(cookie_cps)
        break
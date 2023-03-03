from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import os
import time


# Keep browser up
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# Constants
EMAIL = os.environ.get("EMAIL")
LINKED_PASS = os.environ.get("LINKED_PASS")
URL = "https://www.linkedin.com/jobs/search/?currentJobId=3429562820&f_AL=true&f_WT=2&geoId=103644278&keywords=solutions%20architect&location=United%20States&refresh=true&start=25"

# Webdriver and get url
service = Service("/home/dk/Documents/chromedriver")
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.maximize_window()
driver.get(URL)

# Sign In
sign_in = driver.find_element(By.XPATH, "/html/body/div[1]/header/nav/div/a[2]")
sign_in.click()
# time.sleep(5)
username = driver.find_element(By.ID, "username")
username.send_keys(EMAIL)
password = driver.find_element(By.ID, "password")
password.send_keys(LINKED_PASS)

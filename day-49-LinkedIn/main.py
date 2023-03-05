from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import os
import time


# Keep browser up
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# Constants
EMAIL = os.environ.get("EMAIL")
LINKED_PASS = os.environ.get("LINKED_PASS")
URL = "https://www.linkedin.com/jobs/search/?currentJobId=3513822138&f_AL=true&f_WT=2&geoId=103644278&keywords=solutions%20architect%20%20intern&location=United%20States&refresh=true"

# Webdriver and get url
service = Service("/home/dk/Documents/chromedriver")
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.maximize_window()
driver.get(URL)

# Sign In
sign_in = driver.find_element(By.XPATH, "/html/body/div[1]/header/nav/div/a[2]")
time.sleep(5)
sign_in.click()
time.sleep(3)
username = driver.find_element(By.ID, "username")
username.send_keys(EMAIL)
password = driver.find_element(By.ID, "password")
password.send_keys(LINKED_PASS)
submit = driver.find_element(By.XPATH, "/html/body/div/main/div[2]/div[1]/form/div[3]/button")
submit.click()

# Locate Apply/Save (working)
time.sleep(5)
save = driver.find_element(By.XPATH, "/html/body/div[5]/div[3]/div[4]/div/div/main/div/section[2]/div/div[2]/div[1]/div/div[1]/div/div[1]/div[1]/div[3]/div/button")
save.click()

# Applying/saving all listings
all_listings = driver.find_elements(By.CSS_SELECTOR, ".job-card-container--clickable")

for listing in all_listings:
    print("saved")
    listing.click()
    time.sleep(3)

    # Locate save button
    try:
        save_button = driver.find_element(By.CSS_SELECTOR, ".jobs-save-button")
        save_button.click()
        time.sleep(5)
    except NoSuchElementException:
        print("error")
        continue
time.sleep(5)

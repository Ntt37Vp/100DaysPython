from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time


chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

URL = "https://fast.com/"
service = Service(executable_path="/home/dk/Documents/chromedriver")
driver = webdriver.Chrome(service=service, options=chrome_options)

# Run
driver.maximize_window()
driver.get(URL)
time.sleep(15)

# Get download speed
down_speed = driver.find_element(By.ID, "speed-value")
print(f"Download: {down_speed.text}")

# Click Show More and get upload speed
show_more = driver.find_element(By.ID, "show-more-details-link")
show_more.click()
time.sleep(30)
up_speed = driver.find_element(By.ID, "upload-value")
print(f"Upload: {up_speed.text}")

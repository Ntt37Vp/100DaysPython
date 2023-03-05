from selenium import webdriver
from selenium.webdriver.common.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep
import os


chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

FB_EMAIL = os.environ.get("EMAIL")
FB_PASS = os.environ.get("FB_PASS")
URL = "http://www.tinder.com"
service = Service("/home/dk/Documents/chromedriver")
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.maximize_window()
driver.get(URL)

sleep(2)
login_btn = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a/div[2]/div[2]")
login_btn.click()

sleep(2)
fb_login = driver.find_element(By.XPATH, "/html/body/div[2]/main/div/div/div[1]/div/div/div[3]/span/div[2]/button/div[2]/div[2]/div/div")
fb_login.click()

print("skip project")

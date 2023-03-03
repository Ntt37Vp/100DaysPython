from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys


chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

target = "https://testpages.herokuapp.com/styled/basic-html-form-test.html"
service = Service("/home/dk/Documents/chromedriver")

driver = webdriver.Chrome(service=service, options=chrome_options)
driver.maximize_window()
driver.get(target)
username = driver.find_element(By.NAME, "username")
username.send_keys("sample_user")
username.send_keys(Keys.TAB)
password = driver.find_element(By.NAME, "password")
password.send_keys("password")
username.send_keys(Keys.TAB)
submit = driver.find_element(By.NAME, "submitbutton")
submit.click()

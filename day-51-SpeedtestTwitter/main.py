from selenium import webdriver
from selenium.webdriver.common.service import Service
from selenium.webdriver.common.by import By
import os
import time
import tweepy


PROMISED_UP = 100
PROMISED_DOWN = 100
URL = "https://www.speedtest.net/"
TWITTER = "https://twitter.com/i/flow/login"
TWITTER_EMAIL = os.environ.get("TWITTER_EMAIL")
TWITTER_PASS = os.environ.get("TWITTER_PASS")
SERVICE = Service("/home/dk/Documents/chromedriver")
DRIVER = webdriver.Chrome(service=SERVICE)


class InternetSpeedTwitter:
    def __init__(self):
        self.up = 0
        self.down = 0
        self.driver = webdriver.Chrome(service=SERVICE)

    def test_speed(self):
        self.driver.get(URL)
        time.sleep(3)
        go_button = self.driver.find_element(By.CLASS_NAME, "start-text")
        go_button.click()
        time.sleep(60)
        self.up = self.driver.find_element(By.XPATH, "/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span")
        self.down = self.driver.find_element(By.XPATH, "/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span")

    def tweet(self, message):
        # use tweepy
        pass


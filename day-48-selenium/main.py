from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# chrome_options = Options
# chrome_options.add_experimental_option("detach", True)

chrome_driver_path = "/home/dk/Documents/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)


driver.get("https://www.amazon.com/Duo-Evo-Plus-esterilizadora-vaporizador/dp/B07W55DDFB/ref=sr_1_4?qid=1597660904")

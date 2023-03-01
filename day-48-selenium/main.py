from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

service = Service('C:/Users/DK/Documents/DEV/chromedriver.exe')
driver = webdriver.Chrome(service=service, options=chrome_options)

product_url = "https://www.amazon.com/Yubico-YubiKey-USB-Authentication-Security/dp/B07HBD71HL/ref=pd_ci_mcx_mh_mcx_views_0?pd_rd_w=n4IRA&content-id=amzn1.sym.1bcf206d-941a-4dd9-9560-bdaa3c824953&pf_rd_p=1bcf206d-941a-4dd9-9560-bdaa3c824953&pf_rd_r=21MF8MXSH971N5DT330E&pd_rd_wg=sSQRe&pd_rd_r=4bd2c343-aac5-4e7d-ba4b-93b249506dc1&pd_rd_i=B07HBD71HL&th=1"

driver.get(product_url)
price = driver.find_element(by="class name", value="a-offscreen").get_attribute("textContent")
price_float = float(price.split("$")[1])
print(price_float)

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)
driver.get("https://orteil.dashnet.org/cookieclicker/")
time.sleep(5)

eng = driver.find_element(By.CSS_SELECTOR, "#langSelect-EN")
eng.click()
time.sleep(5)
cookie = driver.find_element(By.ID, "bigCookie")

while True:
    cookie.click()
import threading
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)
driver.get("https://orteil.dashnet.org/cookieclicker/")
time.sleep(5)

eng = driver.find_element(By.CSS_SELECTOR, "#langSelect-EN")
eng.click()
time.sleep(5)
cookie = driver.find_element(By.ID, "bigCookie")

## TIME LIMIT

# def upgrade():
#     while True:
#         time.sleep(5)
#
#         buys = driver.find_elements(By.CSS_SELECTOR, ".crate.upgrade.enabled, .product.unlocked.enabled")
#         print(len(buys))
#
#         for i in buys:
#             i.click()
#             print("Clicked")
#
#
# thread_upgrades = threading.Thread(target=upgrade)0l
# thread_upgrades.daemon = True
# thread_upgrades.start()

while True:
    cookie.click()
    buys = driver.find_elements(By.CSS_SELECTOR, ".crate.upgrade.enabled, .product.unlocked.enabled")
    print(len(buys))

    for i in buys:
        i.click()
        print("Clicked")

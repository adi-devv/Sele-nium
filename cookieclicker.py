import time

from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=options)
driver.get('https://orteil.dashnet.org/cookieclicker/')
time.sleep(5)

eng = driver.find_element(By.CSS_SELECTOR, '#langSelect-EN')
eng.click()
time.sleep(5)
cookie = driver.find_element(By.ID, 'bigCookie')

while True:
    cookie.click()
    buys = driver.find_elements(By.CSS_SELECTOR, '.crate.upgrade.enabled, .product.unlocked.enabled')
    print(len(buys))

    for i in buys:
        i.click()
        print('Clicked')

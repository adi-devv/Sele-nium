import time

from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option('deta ch', True)

options.add_argument(r'user-data-dir=C:\Users\aadit\AppData\Local\Google\Chrome\User Data')  # Update this path

driver = webdriver.Chrome(options=options)
driver.get(
    'https://www.instagram.com/johnderting/followers/'
)

time.sleep(2)

count = driver.find_element(By.XPATH, '//a[@href="/johnderting/followers/"]')
count.click()

time.sleep(2)

flws = driver.find_elements(By.CSS_SELECTOR, '._acan._acap._acas._aj1-._ap30')
for i in flws:
    try:
        i.click()
    except Exception as e:
        print('Exception',e)

        continue

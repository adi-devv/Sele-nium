from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome()
driver.get('https://en.wikipedia.org/wiki/Main_Page')
a = driver.find_element(By.CSS_SELECTOR, value='#articlecount a')

print(a.text)
a.click()
driver.back()
Dage = driver.find_element(By.LINK_TEXT, value='Dagestan')
Dage.click()

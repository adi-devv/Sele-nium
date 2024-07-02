import time
from selenium import webdriver
from selenium.webdriver.common.by import By

from bs4 import BeautifulSoup
import requests

resp = requests.get("https://appbrewery.github.io/Zillow-Clone/")
soup = BeautifulSoup(resp.text, 'html.parser')

links = [i['href'] for i in soup.select('a.StyledPropertyCardDataArea-anchor')]
address = [i.text.strip() for i in soup.select('address[data-test="property-card-addr"]')]
cost = [i.text.strip() for i in soup.select('span.PropertyCardWrapper__StyledPriceLine')]

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)
driver.get(
    "https://docs.google.com/forms/d/1nVfEwfRetDzcjuXIbOQx-wFUfZ6HQ4AYtIT7WLQMWEc/viewform"
)

for i, v in enumerate(links):
    time.sleep(2)
    entries = driver.find_elements(By.CSS_SELECTOR, ".whsOnd.zHQkBf")
    print(entries)
    submit = driver.find_element(By.CSS_SELECTOR, ".NPEfkd.RveJvd.snByac")
    entries[0].click()
    entries[0].send_keys(address[i])
    entries[1].click()
    entries[1].send_keys(cost[i])
    entries[2].click()
    entries[2].send_keys(v)
    submit.click()
    driver.find_element(By.LINK_TEXT, "Submit another response").click()
driver.quit()
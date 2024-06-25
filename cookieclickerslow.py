import threading
import time

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)
driver.get("https://orteil.dashnet.org/cookieclicker/")

wait = WebDriverWait(driver, 10)
eng = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#langSelect-EN")))[0]

eng.click()
time.sleep(5)
cookie = wait.until(EC.presence_of_all_elements_located((By.ID, "bigCookie")))[0]


## TIME LIMIT

def upgrade():
    try:
        while True:
            time.sleep(5)

            u = driver.find_elements(By.CSS_SELECTOR, ".crate.upgrade.enabled")
            p = driver.find_elements(By.CSS_SELECTOR, ".product.unlocked.enabled")
            print(p)
            for i in u + p:
                driver.execute_script("arguments[0].scrollIntoView();", i)
                i.click()
                print("Clicked")
    except Exception as e:
        print(e)


thread_upgrades = threading.Thread(target=upgrade)
thread_upgrades.daemon = True
thread_upgrades.start()

while True:
    cookie.click()

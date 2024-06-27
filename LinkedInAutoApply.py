import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

options.add_argument(r"user-data-dir=C:\Users\aadit\AppData\Local\Google\Chrome\User Data")  # Update this path

driver = webdriver.Chrome(options=options)
driver.get(
    "https://www.linkedin.com/jobs/search/?f_AL=true&f_E=1&f_WT=2&geoId=102713980&keywords=Python&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true"
)

wait = WebDriverWait(driver, 10)
jobs = wait.until(
    EC.presence_of_all_elements_located((By.XPATH, '//*[@id="main"]/div/div[2]/div[1]/div/ul/li/div/div')))


def check(criteria, val, parent=driver):
    try:
        print(parent)
        element = parent.find_element(criteria, val)
        return element
    except Exception as e:
        print(e)
        return None


def check_all(criteria, val, parent=driver):
    try:
        print(parent)
        elements = parent.find_elements(criteria, val)
        return elements
    except Exception as e:
        print(e)
        return None


for j in jobs:
    j.click()
    time.sleep(0.2)
    easyapply = check(By.CLASS_NAME, "jobs-apply-button--top-card")
    if easyapply:
        easyapply.click()
        print("Started", easyapply.get_attribute("aria-label"))
    else:
        close = check(By.XPATH, './/button', j)
        close.click()
        print("Closed", jobs.index(j))
        continue

    continueApplying = check(By.CSS_SELECTOR,
                             ".jobs-apply-button artdeco-button artdeco-button--3 artdeco-button--primary ember-view")
    if continueApplying:
        continueApplying.click()

    b = True
    while b is True:
        time.sleep(3)
        proceed = check_all(By.CSS_SELECTOR, '.display-flex.justify-flex-end.ph5.pv4 button')[-1]
        if proceed.get_attribute("aria-label") == 'Submit application':
            check(By.CLASS_NAME, 'job-details-easy-apply-footer__section').click()
            b = False
        proceed.click()

    close2 = wait.until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div/div/button'))
    )
    close2.click()
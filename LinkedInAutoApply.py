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


def wait_for_element(locator, context=driver):
    return WebDriverWait(context, 10).until(
        EC.element_to_be_clickable(locator)
    )


def wait_for_elements(locator, context=driver):
    return WebDriverWait(context, 10).until(
        EC.presence_of_all_elements_located(locator)
    )


def check(criteria, val, parent=driver):
    try:
        print(parent)
        element = parent.find_element(criteria, val)
        driver.execute_script("arguments[0].scrollIntoView({behavior:'smooth'});", element)

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

time.sleep(3)
jobs = wait_for_elements((By.XPATH, '//*[@id="main"]/div/div[2]/div[1]/div/ul/li/div/div'))

for j in jobs:
    driver.execute_script("arguments[0].scrollIntoView({behavior:'smooth'});", j)

    j.click()
    time.sleep(1)
    easyApply = check(By.CLASS_NAME, "jobs-apply-button--top-card")
    if easyApply:
        easyApply.click()
        print("Started", easyApply.get_attribute("aria-label"))
    else:
        close = check(By.XPATH, './/button', j)
        close.click()
        print("Closed", jobs.index(j))
        continue

    continueApplying = check(By.XPATH, '/html/body/div[3]/div/div/div[3]/div/div/button')
    if continueApplying:
        continueApplying.click()

    b = True
    while b is True:
        time.sleep(2)
        proceed = check_all(By.CSS_SELECTOR, '.display-flex.justify-flex-end.ph5.pv4 button')[-1]

        if proceed.get_attribute("aria-label") == 'Submit application':
            flw = check(By.CLASS_NAME, 'job-details-easy-apply-footer__section')
            if flw:
                flw.click()

            b = False
        proceed.click()
    else:
        time.sleep(2)
        close2 = check(By.XPATH, "//*[@aria-label='Dismiss']")
        close2.click()
    time.sleep(1)

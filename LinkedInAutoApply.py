import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)

options.add_argument(r'user-data-dir=C:\Users\aadit\AppData\Local\Google\Chrome\User Data')  # Update this path

driver = webdriver.Chrome(options=options)
driver.get(
    'https://www.linkedin.com/jobs/search/?f_AL=true&f_E=1&f_WT=2&geoId=102713980&keywords=Python&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true'
)


def wait_for(by, value, condition=EC.element_to_be_clickable):
    return WebDriverWait(driver, 10).until(condition((by, value)))


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


time.sleep(3)
jobs = wait_for(By.XPATH, '//*[@id="main"]/div/div[2]/div[1]/div/ul/li/div/div', EC.presence_of_all_elements_located)
print(len(jobs))
for j in jobs:
    try:
        driver.execute_script('arguments[0].scrollIntoView({ behavior: "smooth", block: "start" });', j)
        time.sleep(2)
        j.click()
        time.sleep(1)
        easyApply = check(By.CLASS_NAME, 'jobs-apply-button--top-card')
        if easyApply:
            easyApply.click()
            print('Started', easyApply.get_attribute('aria-label'))
        else:
            close = check(By.XPATH, './/button', j)
            close.click()
            print('Closed', jobs.index(j))
            continue

        continueApplying = check(By.XPATH, '/html/body/div[3]/div/div/div[3]/div/div/button')
        if continueApplying:
            time.sleep(1)
            continueApplying.click()

        b = True
        while b is True:
            proceed = check_all(By.CSS_SELECTOR, '.display-flex.justify-flex-end.ph5.pv4 button')[-1]
            driver.execute_script('arguments[0].scrollIntoView({ behavior: "smooth", block: "end" });', proceed)
            time.sleep(2)
            if proceed.get_attribute('aria-label') == 'Submit application':
                flw = check(By.CLASS_NAME, 'job-details-easy-apply-footer__section')
                if flw:
                    flw.click()

                b = False
            proceed.click()
        else:
            time.sleep(2)
            close2 = check(By.XPATH, '//*[@aria-label="Dismiss"]')
            close2.click()
        time.sleep(1)
    except Exception as e:
        print(e)

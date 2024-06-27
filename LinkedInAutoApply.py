from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

#options.add_argument(r"user-data-dir=C:\Users\aadit\AppData\Local\Google\Chrome\User Data")  # Update this path
options.add_argument("profile-directory=Person 1")

driver = webdriver.Chrome(options=options)
driver.get(
    "https://www.linkedin.com/jobs/search/?currentJobId=3959633573&f_AL=true&f_E=1&f_WT=2&geoId=102713980&keywords=Python&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true"
)

jobs = driver.find_elements(By.XPATH, '//*[@id="main"]/div/div[2]/div[1]/div/ul/li/div/div')


def check(criteria, val):
    try:
        button = driver.find_element(criteria, val)
        return button
    except Exception as e:
        print(e)
        return False


for j in jobs:
    j.click()
    easyApply = check(By.CLASS_NAME, "jobs-apply-button--top-card")
    if easyApply:
        easyApply.click()
        continueApplying = check(By.CLASS_NAME, "jobs-apply-button artdeco-button artdeco-button--3 artdeco-button--primary ember-view")
        if continueApplying:
            continueApplying.click()

        while True:
            next = check(By.CSS_SELECTOR, ".display-flex.justify-flex-end.ph5.pv4 ")



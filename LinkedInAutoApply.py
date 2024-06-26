from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

options.add_argument(r"user-data-dir=C:\Users\aadit\AppData\Local\Google\Chrome\User Data")  # Update this path
options.add_argument("profile-directory=Default")

driver = webdriver.Chrome(options=options)
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3955544415&f_AL=true&f_E=1&f_WT=2&geoId=102713980&keywords=Python&origin=JOB_SEARCH_PAGE_LOCATION_AUTOCOMPLETE&refresh=true&spellCorrectionEnabled=true#HYM")


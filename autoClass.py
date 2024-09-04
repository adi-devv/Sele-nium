import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)

options.add_argument(r'user-data-dir=C:\Users\aadit\AppData\Local\Google\Chrome\User Data')  # Update this path

driver = webdriver.Chrome(options=options)

time_table = {
    'Monday': {
        '1:15': 'CSA4005', '2:50': 'MAT3003'
    },
    'Tuesday': {
        '8:30': 'MAT3003'
    },
    'Thursday': {
        '8:30': 'MAT3003', '2:50': 'HUM0001',
    },
    'Friday': {
        '1:15': 'CSA4005',
    },
}

classroomLinks = {
    ''
}

driver.get(
    'https://www.linkedin.com/jobs/search/?f_AL=true&f_E=1&f_WT=2&geoId=102713980&keywords=Python&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true'
)

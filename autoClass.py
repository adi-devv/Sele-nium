import time
from datetime import datetime

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
options.add_argument(r'user-data-dir=C:\Users\aadit\AppData\Local\Google\Chrome\User Data')
driver = webdriver.Chrome(options=options)

time_table = {
    'Monday': {
        '8:30': 'CSA3004', '10:05': 'CSE3001', '11:40': 'CSA4002', '1:15': 'CSA4005', '2:50': 'MAT3003'
    },
    'Tuesday': {
        '8:30': 'MAT3003', '10:05': 'CSE3010', '11:40': 'CSG2003',
    },
    'Wednesday': {'8:30': 'CSA3004', '10:05': 'CSE3001', '11:40': 'CSA4002'},
    'Thursday': {
        '8:30': 'MAT3003', '10:05': 'CSE3010', '11:40': 'CSG2003', '2:50': 'HUM0001',
    },
    'Friday': {
        '10:05': 'CSE3001', '11:40': 'CSA4002', '1:15': 'CSA4005',
    },
}

classroomCodes = {
    'CSA3004': '',
    'CSA4002': '',
    'CSA4005': 'NzEwMzE3MjkyODcw',
    'CSE3001': '',
    'CSE3010': '',
    'CSG2003': '',
    'HUM0001': 'NzEwNzQ3ODg5NjY0',
    'MAT3003': 'NzEwNjMyODcwNzA1'
}


def startMeeting(link):
    driver.get(link)


while True:
    now = datetime.now()
    today = now.strftime("%A")
    current_time = now.strftime("%H:%M")

    for day, table in time_table.items():
        if day == today:
            for slot, subject in table.items():


    time.sleep(300)

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

def wait_for_element(locator, context=driver):
    return WebDriverWait(context, 10).until(
        EC.element_to_be_clickable(locator)
    )
def wait_for_elements(locator, context=driver):
    return WebDriverWait(context, 20).until(
        EC.presence_of_all_elements_located(locator)
    )

def startMeeting(link):
    if link is None:
        print("Classroom Not Yet Created")
        return
    driver.get(link)
    joinButton = wait_for_element((By.XPATH,'//*[@id="yDmH0d"]/c-wiz/div[2]/div/div[7]/div[2]/aside/div/div[2]/div/div[2]/div/a'))
    joinButton.click()
    time.sleep(5)
    driver.scro
    mic_button = wait_for_element((By.CSS_SELECTOR, 'div[aria-label="Turn off microphone"]'))
    cam_button = wait_for_element((By.CSS_SELECTOR, 'div[aria-label="Turn off camera"]'))
    if mic_button.get_attribute('data-is-muted') == 'false':
        mic_button.click()

    # Toggle the camera button
    if cam_button.get_attribute('data-is-muted') == 'false':
        cam_button.click()
    joinNow = wait_for_element((By.CSS_SELECTOR,'.UywwFc-LgbsSe.UywwFc-LgbsSe-OWXEXe-dgl2Hf.q9a6Xc.tusd3.IyLmn'))
    joinNow.click()
    #
    # mute_hide = wait_for_element((By.XPATH, '//*[@jsname="BOHaEe"]'))
    # if mute_hide:
    #         print(mute_hide,'clicked')
    #         mute_hide.click()
    # else:
    #     print("No elements found to mute or hide.")


while True:
    now = datetime.now()
    today = now.strftime("%A")
    current_time = now.strftime("%H:%M")

    for day, table in time_table.items():
        if day == today:
            for slot, subject in table.items():
                if current_time == slot:
                    startMeeting('https://classroom.google.com/u/2/c/' + classroomCodes[subject])

    startMeeting('https://classroom.google.com/u/2/c/NzEwMzE3MjkyODcw')
    time.sleep(300)

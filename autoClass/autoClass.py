import time
from datetime import datetime, timedelta
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging

logging.basicConfig(filename='automation.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
options.add_argument(r'user-data-dir=C:\Users\<YOUR DEVICE NAME>\AppData\Local\Google\Chrome\User Data')
driver = webdriver.Chrome(options=options)

time_table = {                  #UPDATE THE TIMETABLE
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

classroomCodes = {                #UPDATE THE CLASSROOM CODES
    'CSA3004': 'NzEwOTkwMDMxNDQw',  # Data Visualization
    'CSA4002': None,  # Artificial Neural Networks
    'CSA4005': 'NzEwMzE3MjkyODcw',  # Expert Systems and Fuzzy Logic
    'CSE3001': 'NzEwOTQzMzc4MTM1',  # Database Management Systems
    'CSE3010': 'NzEwOTQ0MjU3NTM1',  # Computer Vision
    'CSG2003': 'NzA1NTU0MzUwNzAz',  # Human Computer Interaction
    'HUM0001': 'NzEwNzQ3ODg5NjY0',  # Ethics And Values
    'MAT3003': 'NzEwNjMyODcwNzA1',  # Probability, Statistics and Reliability
}


def wait_for(by, value, condition=EC.element_to_be_clickable):
    try:
        return WebDriverWait(driver, 10).until(condition((by, value)))
    except Exception as e:
        logging.error(f"Error waiting for element {by} - {value}: {e}")
        raise

def startMeeting(link):
    if link is None:
        print("Classroom Not Yet Created")
        return
    link = 'https://classroom.google.com/u/2/c/' + link
    driver.get(link)

    try:
        joinButton = wait_for(
            By.XPATH, '//*[@id="yDmH0d"]/c-wiz/div[2]/div/div[7]/div[2]/aside/div/div[2]/div/div[2]/div/a')
        joinButton.click()

        time.sleep(5)
        driver.switch_to.window(driver.window_handles[-1])

        mute_hide = wait_for(By.XPATH, '//*[@jsname="BOHaEe"]', EC.presence_of_all_elements_located)[:2]
        for i in mute_hide:
            if i.get_attribute("data-is-muted") == "false":
                i.click()

        joinNow = wait_for(By.CSS_SELECTOR, '.UywwFc-LgbsSe.UywwFc-LgbsSe-OWXEXe-dgl2Hf.q9a6Xc.tusd3.IyLmn')
        joinNow.click()

    except Exception as e:
        print(e)


def withinSlot(nowT, slot):
    try:
        slotT = datetime.strptime(slot, "%H:%M")
        endT = slotT + timedelta(minutes=90)
        return slotT.time() <= nowT.time() <= endT.time()
    except ValueError as ve:
        logging.error(f"Error parsing time slot: {slot} - {ve}")
        return False


while True:
    try:
        now = datetime.now()
        today = now.strftime("%A")
        current_time = now.strftime("%H:%M")

        for day, table in time_table.items():
            if day == today:
                for slot, subject in table.items():
                    if withinSlot(now, slot):
                        if len(driver.window_handles) > 1:
                            driver.close()
                        startMeeting(classroomCodes.get(subject))


    except Exception as e:
        logging.error(f"Error in the main loop: {e}")
    time.sleep(60)

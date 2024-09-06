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

time_table = {                  #UPDATE THE TIMETABLE 24 HOUR FORMAT
    'Monday': {
        '8:30': 'CSA3004', '10:05': 'CSE3001', '13:15': 'CSA4005', '14:50': 'MAT3003'
    },
    'Tuesday': {
        '8:30': 'MAT3003', '10:05': 'CSE3010', '11:40': 'CSG2003',
    },
    'Wednesday': {
        '8:30': 'CSA3004', '11:40': 'CSA4002'
    },
    'Thursday': {
        '8:30': 'MAT3003', '2:50': 'HUM0001',
    },
    'Friday': {
        '10:05': 'CSE3001', '11:40': 'CSA4002',
    },
}

classroomCodes = {#UPDATE THE CLASSROOM CODES
    'CSA3004': 'NzEwOTkwMAMxNDQw',  # Data Visualization
    'CSA4002': '',  # Artificial Neural Networks
    'CSA4005': '',  # Expert Systems and Fuzzy Logic
    'CSE3001': '',  # Database Management Systems
    'CSE3010': '',  # Computer Vision
    'CSG2003': '',  # Human Computer Interaction
    'HUM0001': '',  # Ethics And Values
    'MAT3003': '',  # Probability, Statistics and Reliability
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
    print("Starting meeting")
    link = 'https://classroom.google.com/u/2/c/' + link
    driver.get(link)
    print("Link opened")

    try:
        joinButton = wait_for(
            By.XPATH, '//*[@id="yDmH0d"]/c-wiz/div[2]/div/div[7]/div[2]/aside/div/div[2]/div/div[2]/div/a')
        driver.execute_script('arguments[0].scrollIntoView({ behavior: "smooth", block: "end" });', joinButton)

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


while True:
    try:
        now = datetime.now()
        today = now.strftime("%A")
        current_time = now.strftime("%H:%M")

        for day, table in time_table.items():
            if day == today:
                for slot, subject in table.items():
                    slotT = datetime.combine(now.date(), datetime.strptime(slot, "%H:%M").time())
                    endT = slotT + timedelta(minutes=90)
                    if slotT.time() <= now.time() <= endT.time():
                        if len(driver.window_handles) > 1:
                            driver.close()
                        driver.switch_to.window(driver.window_handles[0])
                        startMeeting(classroomCodes.get(subject))

                        timer = (endT-now).total_seconds()
                        time.sleep(timer)

    except Exception as e:
        logging.error(f"Error in the main loop: {e}")
    time.sleep(60)
    print("running")

import time
from datetime import datetime, timedelta
import logging
from notmgr import notmgr
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

logging.basicConfig(filename='automation.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

notmgr = notmgr()
options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
options.add_argument(r'user-data-dir=C:\Users\aadit\AppData\Local\Google\Chrome\User Data')
driver = webdriver.Chrome(options=options)

time_table = {
    'Monday': {
        '8:30': 'CSA3004', '10:05': 'CSE3001', '11:40': 'CSA4002', '13:15': 'CSA4005', '14:50': 'MAT3003'
    },
    'Tuesday': {
        '8:30': 'MAT3003', '10:05': 'CSE3010', '11:40': 'CSG2003',
    },
    'Wednesday': {'8:30': 'CSA3004', '10:05': 'CSE3001', '11:40': 'CSA4002'},
    'Thursday': {
        '8:30': 'MAT3003', '10:05': 'CSE3010', '11:40': 'CSG2003', '14:50': 'HUM0001',
    },
    'Friday': {
        '10:05': 'CSE3001', '11:40': 'CSA4002', '13:15': 'CSA4005',
    }
}

classroomCodes = {
    'CSA3004': ['NzEwOTkwMDMxNDQw', 'Data Visualization'],
    'CSA4002': ['NzExMDA4OTM2Nzg1', 'Artificial Neural Networks'],
    'CSA4005': ['NzEwMzE3MjkyODcw', 'Expert Systems and Fuzzy Logic'],
    'CSE3001': ['NzEwOTQzMzc4MTM1', 'Database Management Systems'],
    'CSE3010': ['NzEwOTQ0MjU3NTM1', 'Computer Vision'],
    'CSG2003': ['NzA1NTU0MzUwNzAz', 'Human Computer Interaction'],
    'HUM0001': ['NzEwNzQ3ODg5NjY0', 'Ethics And Values'],
    'MAT3003': ['NzEwNjMyODcwNzA1', 'Probability, Statistics and Reliability']
}


def wait_for(by, value, condition=EC.element_to_be_clickable):
    try:
        return WebDriverWait(driver, 10).until(condition((by, value)))
    except Exception as exc:
        logging.error(f"Error waiting for element {by} - {value}: {exc}")
        raise


def startMeeting(sub):
    code = classroomCodes[sub]
    print("Starting meeting")
    link = 'https://classroom.google.com/u/2/c/' + code[0]
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

        notmgr.notify(f"Meeting Started For {sub} - {code[1]}")

    except Exception as e:
        print(e)
        notmgr.notify(f"Error - couldn't start meeting for {sub} - {code[1]}")


while True:
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
                    try:
                        startMeeting(subject)
                    except Exception as e:
                        logging.error(f"HTTP error during meeting start: {e}")
                    timer = (endT - now).total_seconds()
                    time.sleep(timer)

    time.sleep(60)
    print("running")

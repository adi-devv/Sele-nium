import re
import time

import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
from selenium.common.exceptions import NoSuchElementException

logging.basicConfig(filename='automation.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
options.add_argument(r'user-data-dir=C:\Users\aadit\AppData\Local\Google\Chrome\User Data')

driver = webdriver.Chrome(options=options)


def wait_for(by, value, condition=EC.element_to_be_clickable):
    try:
        return WebDriverWait(driver, 10).until(condition((by, value)))
    except Exception as exc:
        logging.error(f"Error waiting for element {by} - {value}: {exc}")
        raise


file = pd.read_excel(r"D:\Aadit\PESL\Book1.xlsx")
links = ['URL'].dropna().tolist()
data_list = []

for link in links:
    row = file[file['URL'] == link].iloc[0]
    data = {
        'URL': link,
        'Full Name': row['First Name'] + row['Last Name'],
        'Company': row['Company'],
        'Position': row['Position'],
    }

    driver.get(link + '/overlay/contact-info/')
    data['City'] = wait_for(By.CSS_SELECTOR, '.text-body-small.inline.t-black--light.break-words').text.split(',')[0]
    details = wait_for(By.CSS_SELECTOR, '.pv-contact-info__contact-type',
                       EC.presence_of_all_elements_located)[1:]

    for d in details:
        tag = d.find_element(By.XPATH, './h3').text
        val = d.find_element(By.CSS_SELECTOR, '.dFJgnJSrzWlZUXEQJeDCapdaQVlYxovJYzc.t-14').text
        if tag == "Phone":
            match = re.search(r'(\+91)?(\d{10})', val)
            val = match.group(2)
        elif tag == "Website":
            val.strip()[0]
        data[tag] = val
    print(data)
    data_list.append(data)

all_keys = set().union(*(entry.keys() for entry in data_list))
normalized_data = [{key: entry.get(key, '') for key in all_keys} for entry in data_list]
desired_order = ['URL', 'Full Name', 'Company', 'Position', 'City', 'Phone', 'Email', 'Birthday', 'Connected', 'Address', 'Website', 'IM']

df = pd.DataFrame(normalized_data)[desired_order]

with pd.ExcelWriter(r"D:\Aadit\PESL\Book1.xlsx", engine='openpyxl', mode='a', if_sheet_exists='replace') as writer:
    df.to_excel(writer, index=False, header=True, sheet_name='Details')

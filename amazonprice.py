from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

driver.get(
    "https://www.amazon.in/Smoothy-Curvy-Edges-CUTTER-Stainless/dp/B0D2Y21JBK/ref=pd_ci_mcx_mh_mcx_views_0?pd_rd_w=ipBz1&content-id=amzn1.sym.120dbce3-1ee8-4441-9b7e-775b1c676a73%3Aamzn1.symc.ca948091-a64d-450e-86d7-c161ca33337b&pf_rd_p=120dbce3-1ee8-4441-9b7e-775b1c676a73&pf_rd_r=JP4R13XZKEPHHJ0KBXYH&pd_rd_wg=gHJ53&pd_rd_r=106d5200-430b-4ffb-9fa2-7281f3de4dc0&pd_rd_i=B0D2Y21JBK"
)

price = driver.find_element(By.CLASS_NAME, value="a-price-whole")
print(price.text)

searchbar = driver.find_element(By.ID, value="twotabsearchtextbox")
searchbar.send_keys("Black Sport Shoes", Keys.ENTER)


# A new Tab...
driver.execute_script("window.open('');")
driver.switch_to.window(driver.window_handles[1])
driver.get("https://secure-retreat-92358.herokuapp.com/")

FN = driver.find_element(By.NAME, "fName")
LN = driver.find_element(By.NAME, "lName")
email = driver.find_element(By.NAME, "email")
Butt = driver.find_element(By.TAG_NAME, "button")

FN.send_keys("Ianc")
LN.send_keys("Noonesson")
email.send_keys("IancSonsonSon@gmail.com")
Butt.send_keys(Keys.ENTER)

time.sleep(5)
driver.switch_to.window(driver.window_handles[0])
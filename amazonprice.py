from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome()
driver.get("https://www.amazon.in/Smoothy-Curvy-Edges-CUTTER-Stainless/dp/B0D2Y21JBK/ref=pd_ci_mcx_mh_mcx_views_0?pd_rd_w=ipBz1&content-id=amzn1.sym.120dbce3-1ee8-4441-9b7e-775b1c676a73%3Aamzn1.symc.ca948091-a64d-450e-86d7-c161ca33337b&pf_rd_p=120dbce3-1ee8-4441-9b7e-775b1c676a73&pf_rd_r=JP4R13XZKEPHHJ0KBXYH&pd_rd_wg=gHJ53&pd_rd_r=106d5200-430b-4ffb-9fa2-7281f3de4dc0&pd_rd_i=B0D2Y21JBK")

price = driver.find_element(By.CLASS_NAME, value="a-price-whole")
print(price.text)

searchbar = driver.find_element(By.ID, value="twotabsearchtextbox")
print(searchbar.tag_name)

# driver.close()
# driver.quit()
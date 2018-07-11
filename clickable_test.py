from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome(executable_path="/Users/kztmr/Downloads/chromedriver")
driver.set_window_size(500, 600)

driver.get("http://yvsc.jp/")
driver.execute_script("window.scrollTo(0, 3500);")
time.sleep(3)
if EC.element_to_be_clickable('//img[@alt="山形銀行"]'):
  print("This button is clickable.")
  driver.find_element_by_xpath('//img[@alt="山形銀行"]').click()

# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

import time

PATH = "/Users/kyouka/Desktop/chromedriver"
driver =webdriver.Chrome(PATH)
driver.get("https://www.google.com/")
#https://www.youtube.com/watch?v=b5jt2bhSeXs&t=302s
search = driver.find_element_by_name("q");
search.send_keys("Test")
search.send_keys(Keys.RETURN)
try:
    element = WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.ID,"search"))
    )
    elements = element.find_elements_by_class_name("hlcw0c")
    for elements in elements:
        data=elements.find_element_by_class_name("g")
        print(data.text)
except:
    driver.quit()
driver.execute_script("window.open('');")
p = driver.current_window_handle
chwd = driver.window_handles
for w in chwd:
    if w!=p:
        driver.switch_to.window(w)
        break
driver.get("https://www.google.com/")
time.sleep(4)
driver.quit()




#driver.get("https://stackoverflow.com/questions/28431765/open-web-in-new-tab-selenium-python")





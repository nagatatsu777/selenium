from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

import time
def login():
    PATH = "/Users/kyouka/Desktop/chromedriver"
    driver =webdriver.Chrome(PATH)
    driver.get("https://blackboard.gwu.edu/")
    #https://www.youtube.com/watch?v=b5jt2bhSeXs&t=302s
    stpass = input("Username?")
    struser = input("Password?")
    user = driver.find_element_by_id("user_id")
    pas = driver.find_element_by_id("password")
    user.send_keys(stpass)
    pas.send_keys(struser)
    pas.send_keys(Keys.RETURN)


    driver.quit()

def log(driver):
    driver.execute_script("window.open('');")
    driver.get("https://blackboard.gwu.edu/")
    stpass = ""
    struser = input("Password?")
    user = driver.find_element_by_id("user_id")
    pas = driver.find_element_by_id("password")
    user.send_keys(stpass)
    pas.send_keys(struser)
    pas.send_keys(Keys.RETURN)

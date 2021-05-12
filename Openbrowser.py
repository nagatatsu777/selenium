from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from blackboardlogin import log
import time
def openwindow():
    class Key:
        def __init__(self,word):
            self.word = word
        def returnLink(self,numb):
            return self.word[numb]


    PATH = ""
    driver =webdriver.Chrome(PATH)
    driver.get("https://www.google.com/")
    #https://www.youtube.com/watch?v=b5jt2bhSeXs&t=302s
    search = driver.find_element_by_name("q");

    fortest = ["https://blackboard.gwu.edu/","https://blackboard.gwu.edu/","https://blackboard.gwu.edu/","https://blackboard.gwu.edu/","https://blackboard.gwu.edu/",]

    for i in range(0,len(fortest)):
        driver.execute_script("window.open('');")
    ke = Key(fortest)
    p = driver.current_window_handle
    chwd = driver.window_handles
    i=0
    log(driver)
    for w in chwd:
        if w!=p:

            driver.switch_to.window(w)
            driver.get(ke.returnLink(i))
            i+=1
    return driver






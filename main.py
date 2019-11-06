# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 20:56:50 2019

@author: kshubham506
"""
from selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()

def typestart():
    print("\n\nStarted Main Script")

    wait(browser, 400).until(EC.visibility_of_element_located((By.CLASS_NAME, "place-wrapper")))
    
    try:
        input("\n\nPress any key when count turns to 0 ")
    except:
        pass
    
    elem=browser.find_element_by_class_name('place-wrapper')
    elem1=elem.find_element_by_class_name('place')
    allspanItems=elem1.get_attribute('innerHTML')
    
    soup = BeautifulSoup(allspanItems,'html.parser')
    allItems=soup.findAll('span')
    
    inp=browser.find_element_by_tag_name('input')
    for i in allItems:
#        sleep(0.1)
        inp.send_keys(i.text)
        inp.send_keys(Keys.SPACE)

    print("\n\nYou Won...")
    #browser.quit()
    
def init():
    
    print("Initializing....Don't close the browser which is going to be opened.")
    
    username=input("\nType in your user name to use on 10fastFIngersfast Multiplayer : ")
    
    browser.get("https://10fastfingers.com/multiplayer")
    elem=browser.find_element_by_tag_name('iframe')
    
    wait(browser, 10).until(EC.frame_to_be_available_and_switch_to_it(elem))

    uname=browser.find_element_by_id('username')
    uname.send_keys(username)
    uname.send_keys(Keys.ENTER)
    
    typestart()
    
    
    
init()
    

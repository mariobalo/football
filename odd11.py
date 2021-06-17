# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 10:20:07 2020

@author: LI
"""

import datetime as dt
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

import pandas as pd
import yaml

kk= 12
def sig(game_url):
    option = Options()
    option.add_argument('--headless')
    driver = webdriver.Chrome(options=option)
    driver.get( game_url)
    time.sleep(0.3)
    
    if "英超" in driver.find_elements_by_class_name("centerGameInfo")[0].find_elements_by_tag_name("p")[0].text:
        
        print(driver.find_elements_by_class_name("centerGameInfo")[0].find_elements_by_tag_name("p")[0].text +" " + driver.find_elements_by_class_name("enName")[0].text+ " vs " + driver.find_elements_by_class_name("enName")[1].text)
    
    

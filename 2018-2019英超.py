# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 13:14:46 2020

@author: LI
"""

import datetime as dt
from selenium import webdriver
import time
import pandas as pd
from odd import single_game

league = "2018/2019英超"

option = webdriver.ChromeOptions()
option.add_argument('--headless')
driver = webdriver.Chrome(chrome_options=option)

fff = pd.DataFrame()
ddd = dt.date(2018, 8, 10)

end_date = dt.date(2018, 8, 13)

url_base = 'http://odds.sports.sina.com.cn/liveodds/match_search.php?date='

while ddd < end_date:
    
    url = url_base + str(ddd)
    driver.get(url)
    time.sleep(1)
    games = driver.find_elements_by_xpath("//*[@href]")[1:]
    for i in range(int(len(games)/2)):
        game = games[i*2]
        ppp = game.get_attribute('href')
        newwindow =  'window.open("' + ppp +'");'
  
        driver.execute_script(newwindow)
        
        time.sleep(1)
        driver.switch_to.window(driver.window_handles[-1])
        time.sleep(1)
        "======================="
        fq, driver = single_game(league,driver)
        
        if fq is not None:
            fff = pd.concat([fff,fq])
        "======================="
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(1)
        
    ddd = ddd + dt.timedelta(days = 1)
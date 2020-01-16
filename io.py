# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 09:03:50 2020

@author: LI
"""

import datetime as dt
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import pandas as pd
from multiprocessing.dummy import Pool as ThreadPool
#from odd import single_game

def sig(game_url):
    
    option = Options()
    option.add_argument('--headless')
    driver1 = webdriver.Chrome(chrome_options=option)
    
    driver1.get( game_url)
    time.sleep(0.3)
    print(driver1.find_elements_by_class_name("centerGameInfo")[0].find_elements_by_tag_name("p")[0].text +" " + driver1.find_elements_by_class_name("enName")[0].text+ " vs " + driver1.find_elements_by_class_name("enName")[1].text)
    
    if '英超' in driver1.find_elements_by_class_name("centerGameInfo")[0].find_elements_by_tag_name("p")[0].text:
        print('yes')
        time.sleep(0.3)
        companys = driver1.find_elements_by_class_name("oupanFudong")
        companys[1].click()
        time.sleep(1)
        
        table11 = driver1.find_elements_by_id("tipdivOu")[0].find_elements_by_class_name("datachart_table")[0].find_elements_by_tag_name("tbody")[0].find_elements_by_tag_name("tr")
        print(len(table11))
        for j in table11:
            print(j.text)
            
    driver1.quit()
    

option = Options()
option.add_argument('--headless')
driver = webdriver.Chrome(chrome_options=option)
#driver = webdriver.Chrome()

url = 'http://odds.sports.sina.com.cn/liveodds/match_search.php?date=2020-01-12'

driver.get(url)
games = driver.find_elements_by_xpath("//*[@href]")[1:]
games_href = []
for i in range(int(len(games)/2)):
    games_href.append(games[i*2].get_attribute('href'))

st = time.time()    
pool = ThreadPool()
pool.map(sig, games_href)
pool.close()
pool.join()
et = time.time()
print(et - st)
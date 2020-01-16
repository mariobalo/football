# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 10:15:53 2020

@author: LI
"""

import datetime as dt
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import pandas as pd
from odd11 import sig
from multiprocessing.dummy import Pool as ThreadPool


option = Options()
option.add_argument('--headless')
driver = webdriver.Chrome(options=option)

fff = pd.DataFrame()

ddd = dt.date(2019, 8, 18)

end_date = dt.date(2020, 1, 13)

url_base = 'http://odds.sports.sina.com.cn/liveodds/match_search.php?date='

start_time = time.time()

while ddd < end_date:
    print(str(ddd))
    url = url_base + str(ddd)
    try:
        driver.get(url)
    except:
        continue
    else:
        driver.get(url)
    time.sleep(1)
    games = driver.find_elements_by_xpath("//*[@href]")[1:]

    games_href = []
    for i in range(int(len(games)/2)):
        games_href.append(games[i*2].get_attribute('href'))
    
    pool = ThreadPool()
    pool.map(sig, games_href)
    pool.close()
    pool.join()
    
    ddd = ddd + dt.timedelta(days = 1)
    time.sleep(2)

end_time = time.time()   
print(end_time - start_time)
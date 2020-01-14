# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 12:01:59 2020

@author: LI
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Jan  3 15:04:22 2020

@author: LI
"""

import datetime as dt
from selenium import webdriver
import time
import pandas as pd

def single_game(league,driver):    
    
    rounds = driver.find_elements_by_class_name("centerGameInfo")[0].find_elements_by_tag_name("p")[0].text
    
    if league not in rounds:
        return None, driver

    game_dict = pd.DataFrame(columns=('rounds','date','game','home','away','company','win','draw','lose', 'change_time'))
    
    ddd = driver.find_elements_by_id("shijian")[0].text[5:15]
    
    #print(driver.find_elements_by_class_name("centerGameInfo")[0].find_elements_by_tag_name("p")[0].text)
    #print(driver.find_elements_by_class_name("enName")[0].text)
    #print(driver.find_elements_by_class_name("enName")[1].text)
    
    companys = driver.find_elements_by_class_name("oupanFudong")
    time.sleep(1)
    
    for company in companys[1:4]:
        co_name = company.find_elements_by_class_name("bd_r")[0].text
        #co_dict[co_name] = pd.DataFrame(columns=('rounds','date','main','win','draw','lose', 'time'))
        
        time.sleep(1)
        company.click()
        time.sleep(1)
        table11 = driver.find_elements_by_id("tipdivOu")[0].find_elements_by_class_name("datachart_table")[0].find_elements_by_tag_name("tbody")[0].find_elements_by_tag_name("tr")
        
        for j in table11:
            #print(j.text)
            odd_list = j.find_elements_by_tag_name("td")
            hhhh = []
            for ooo in odd_list[0:3]:
                hhhh.append(float(ooo.text[0:4]))
            hhhh.append(dt.datetime.strptime(odd_list[4].text, "%Y-%m-%d %H:%M"))   
             
            game_dict = game_dict.append(pd.DataFrame({'rounds':[rounds],
               'date':[ddd],
               'game':[driver.find_elements_by_class_name("enName")[0].text+ " vs " + driver.find_elements_by_class_name("enName")[1].text],
               'home':[driver.find_elements_by_class_name("enName")[0].text],
               'away':[driver.find_elements_by_class_name("enName")[1].text],
               'company':[co_name],
               'win':hhhh[0],
               'draw':hhhh[1],
               'lose':hhhh[2], 
               'change_time':hhhh[3]}))
        
        driver.find_elements_by_id("tipdivOu")[0].find_elements_by_tag_name('a')[0].click()
    time.sleep(1)
    
    driver.find_elements_by_id("jichu")[0].click()
    jiaozhan_list = driver.find_elements_by_id("jiaozhanBody")[0].find_elements_by_tag_name("tr")
    for jz in jiaozhan_list:
        if ddd in jz.text:
            gggg = []
            for word in jz.text.split(' '):
                gggg.append(word)
    game_dict['resault'] = gggg[6]
    game_dict['score'] = gggg[5]
    
    return game_dict, driver
    



    


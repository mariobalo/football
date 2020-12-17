# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 15:11:54 2020

@author: mario
"""

from simonsc import auth
#login
auth(username="quantresearch", password="quantresearch")


import pandas as pd
from simonsc.api import history_bars

# 获取中国平安 2020-04-20之前10天的交易数据
dt = pd.Timestamp("2020-04-20")
fields=["datetime","open","high","low","close"]
data = history_bars(order_book_ids=["000001.XSHE"], dt=dt, bar_count=10, frequency="1d", fields=fields)

from simonsc.api import get_factor_exposure

dt = pd.Timestamp("2020-09-18")
fields=["datetime","return_mean_5","returns_skew_20","downside_volatility_20"]
order_book_id_list = ["000001.XSHE","000002.XSHE"]
factor_exposure = get_factor_exposure(order_book_ids=order_book_id_list, dt=dt, bar_count=10, fields=fields, frequency="1d")
print(factor_exposure)
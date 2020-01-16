# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 16:57:47 2020

@author: LI
"""

import time
from multiprocessing.dummy import Pool as ThreadPool


def rr(x):
    print(x)
    
    time.sleep(0.9)
    
def pp(x):
    rr(x)

s = time.time()
items = [1,2,3,4]

pool = ThreadPool()
pool.map(pp, items)
pool.close()
pool.join()

e = time.time()

print(e-s)
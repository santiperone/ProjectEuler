# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 21:08:49 2020

@author: santi
"""
from time import time
start = time()
suma = 0
for i in range(1,1000001):
    if str(i) == str(i)[::-1] and f'{i:b}' == f'{i:b}'[::-1]:
        suma += i
print(suma)       
print(time()-start)
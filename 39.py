# -*- coding: utf-8 -*-
"""
Created on Fri May  1 16:37:55 2020

@author: santi
"""

import numpy as np

lista = []

for c in range(0,1000):
    for a in range(0, c):
        p = a + c + np.sqrt(c **2 - a**2)
        if p <= 1000 and p % 1 == 0:
            lista.append(p)

contmax = 0
for p in lista:
    if lista.count(p) > contmax:
        contmax = lista.count(p)
        pmax = p
print(pmax)

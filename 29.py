# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 23:44:51 2020

@author: santi
"""


lista = []
for a in range(2,101):
    for b in range(2,101):
        if a**b not in lista:
            lista.append(a**b)
            
print(len(lista))
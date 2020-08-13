# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 14:53:56 2020

@author: santi
"""

def fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fact(n-1)

suma = 0
for i in str(fact(100)):
    suma += int(i)
print(suma)
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 21:50:46 2020

@author: santi
"""
from mcm import es_primo

i = 2
cont = 0
while cont < 10001:
    if es_primo(i):
        cont += 1
    if cont < 10001:
        i += 1
print(i)
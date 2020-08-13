# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 20:24:52 2020

@author: santi
"""
funcionando = True
i = 2520
while funcionando:
    for p in range(1,21):
        if i % p != 0:
            i += 1
            break




# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 18:13:50 2020

@author: santi
"""
lista = []
numerador = 1
denominador = 1
for a in range(1,10):
    for b in range (1,10):
        for c in range(1,10):
                if (10*b+a)/(10*a+c) == b/c != 1:
                    numerador *= b
                    denominador *= c
                    


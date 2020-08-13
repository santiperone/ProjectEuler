# -*- coding: utf-8 -*-
"""
Created on Sun May  3 23:53:41 2020

@author: santi
"""


import numpy as np

def pentagonal(n):
    return n * (3*n - 1) // 2

def es_pentagonal(n):
    r1 = ((np.sqrt(1+24*n)+1)/6)
    return r1 % 1 == 0 and r1 > 0

def es_hexagonal(n):
    r1 = ((np.sqrt(1+8*n)+1)/4)
    return r1 % 1 == 0 and r1 > 0

def main():
    funcionando = True
    i = 2
    cont = 0
    while funcionando:
        if es_hexagonal(pentagonal(i)):
            cont += 1
            if cont == 2:
                return pentagonal(i)
        i += 1

print(main())
# -*- coding: utf-8 -*-
"""
Created on Mon May  4 00:15:14 2020

@author: santi
"""
import numpy as np

def es_pentagonal(n):
    r1 = ((np.sqrt(1+24*n)+1)/6)
    return r1 % 1 == 0 and r1 > 0

def pentagonal(n):
    return n * (3*n - 1) // 2

def main():
    funcionando = True
    i = 1
    while funcionando:
        Pi = pentagonal(i)
        for j in range(i-1,0,-1):
            Pj = pentagonal(j)
            if es_pentagonal(Pi+Pj) and es_pentagonal(Pi-Pj):
                return Pi-Pj
        i += 1
        
print(main())
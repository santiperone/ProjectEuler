# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 22:57:27 2020

@author: santi
"""
from raiz_perfecta import raiz_perfecta

def pyt_triplet(n):
    """
    returns a*b*c for a pythagorean triplet for which a+b+c = n

    """
    for a in range(1,n):
        for b in range(1,n):
            c = raiz_perfecta((a**2 + b**2))
            if a + b + c == n and c != 0:
                return a*b*c
                

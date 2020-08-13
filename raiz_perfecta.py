# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 23:10:09 2020

@author: santi
"""
def raiz_perfecta(n):
    x = 0
    funcionando = True
    if n == 0:
        raiz = 0
        funcionando = False
        cubo = True
    else:
        while funcionando:
            if x**2 == n:
                funcionando = False
                cubo = True
            elif x**2 > n:
                funcionando = False
                cubo = False
            else:
                x += 1
        raiz = x
    if cubo == False:
        return 0
    elif n >= 0:
        return raiz 
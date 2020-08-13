# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 23:18:07 2020

@author: santi
"""
def es_primo(n):
    """
    Recibe un numero n y dice si es primo.

    """
    if n <= 0:
        return False
    for i in range (2,n):
        if n % i == 0:
            return False
    return True

def quadratic(a,b,n):
    return n**2 + a*n + b

listaprimos = []
for i in range(1,1001):
    if es_primo(i):
        listaprimos.append(i)

maxa = 0
maxb = 0
contmax = 0    
for i in listaprimos:
    for a in [-i,i]:
        for b in listaprimos:
            cont = 0
            n = 0
            while es_primo(quadratic(-a,b,n)):
                cont += 1
                n += 1
            if cont > contmax:
                contmax = cont
                maxa = a
                maxb = b
       
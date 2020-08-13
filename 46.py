# -*- coding: utf-8 -*-
"""
Created on Tue May  5 11:08:30 2020

@author: santi
"""

import numpy as np
from time import time


def es_primo(n):
    """
    Recibe un numero n y dice si es primo.

    """
    for i in range (2,int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def lista_primos(n):
    lista = []
    for i in range(2,n+1):
        if es_primo(i):
            lista.append(i)
    return lista

def main():
    for i in range(1,1000000,2):
        if not es_primo(i):
            cumple = True
            for j in lista_primos(i):
                if np.sqrt((i-j)/2) % 1 == 0:
                    cumple = False
                    pass
            if cumple:
                return i
            
start = time()   
print(main())
print(time() - start)
                
                
        

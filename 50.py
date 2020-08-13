# -*- coding: utf-8 -*-
"""
Created on Fri May  8 11:33:25 2020

@author: santi
"""
from time import time
from lista_primos import lista_primos

start = time()
lista = lista_primos(1000000)

lenmax = 0
sumamax = 0
lastj = len(lista)

for i in range(len(lista)):
    for j in range(i+lenmax,lastj):
        
        if sum(lista[i:j]) < 1000000:
            if sum(lista[i:j]) in lista:
                sumamax = sum(lista[i:j])
                lenmax = j-i
        else:
            lastj = j+1
            break

print(sumamax)
print(time()-start)
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 01:15:51 2020

@author: santi
"""

from mcm import es_primo

def permutaciones(x):
    lista = []
    if len(x) <= 1:
        return x
    else:
        for i in range(len(x)):
            # print(x[i])
            # print(x[:i] + x[i + 1:])
            for p in permutaciones(x[:i] + x[i + 1:]):
                # print(x[i]+p)
                if x[i]+p not in lista:
                    lista.append(x[i]+p)
    
    return(lista)                                

lista = []
for i in range(1000,10000):
    if es_primo(i):
        lista.append(i)

for i in lista:
    for j in permutaciones(str(i))[1:]:
        # print(j)
        if int(j) in lista:
            lista.remove(int(j))
            
lista.remove(1487)
        
listaprimos = []
for i in lista:
    cont = 0
    listav = []
    for j in permutaciones(str(i)):
        j = int(j)
        if es_primo(j) and j > 1000:
            cont += 1
            listav.append(j)
    if cont >= 4:
        listaprimos.append(listav)

listafinal = []            
# for i in listaprimos[7:8]:
for i in listaprimos:
    serie = []
    for j in i:
        if j+3330 in i and j+6660 in i:
            print(str(j)+str(j+3330)+str(j+6660))
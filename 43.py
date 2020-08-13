# -*- coding: utf-8 -*-
"""
Created on Sun May  3 03:11:49 2020

@author: santi
"""

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
                lista.append(x[i]+p)
    
    return(lista)                                

lista = []
for i in permutaciones('0123456789'):
    c1 = int(i[1:4]) % 2 == 0
    c2 = int(i[2:5]) % 3 == 0
    c3 = int(i[3:6]) % 5 == 0
    c4 = int(i[4:7]) % 7 == 0
    c5 = int(i[5:8]) % 11 == 0
    c6 = int(i[6:9]) % 13 == 0
    c7 = int(i[7:10]) % 17 == 0
    if c1 and c2 and c3 and c4 and c5 and c6 and c7:
        lista.append(int(i))

print(sum(lista))
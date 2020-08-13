# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 01:15:51 2020

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
for num in permutaciones('123456789'):
    for i in range(1,7):
        for j in range(i+1,8):
            if int(num[:i]) * int(num[i:j]) == int(num[j:]):
                if int(num[j:]) not in lista:
                    lista.append(int(num[j:]))
print(sum(lista))
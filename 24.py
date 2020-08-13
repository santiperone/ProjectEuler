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

lista = permutaciones(['0','1','2','3','4','5','6','7','8','9'])
print(lista[999999])
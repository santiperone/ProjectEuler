# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 15:47:32 2020

@author: santi
"""


def lista_divisores(n):
    """
    Recibe un numero n y devuelve una lista de sus divisores

    """ 
    lista = []
    for i in range(1,n):
        if n % i == 0:
            lista.append(i)
    return lista

def suma_divisores(n):
    """
    Recibe un numero n y devuelve la suma de sus divisores

    """ 
    suma = 0
    for i in lista_divisores(n):
        suma += i
    return suma

def es_abundante(a):
    return a < suma_divisores(a)

lista = []
lista2 = []


for i in range(12,28123):
    if es_abundante(i):
        lista.append(i)
        
for i in lista:
    for p in lista[lista.index(i):]:
        if (i+p) <= 28123:
            lista2.append(i+p)
            
lista2 = list(dict.fromkeys(lista2))

suma = ((28123*28124)/2) - sum(lista2)

            
        
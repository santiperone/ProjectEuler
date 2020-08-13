# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 20:37:29 2020

@author: santi
"""

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

def lista_factores(n):
    residuo = n
    lista = []
    for i in lista_primos(int(n**0.5)):
        cont = 0
        while residuo % i == 0:
            residuo = residuo / i
            cont += 1
            lista.append(i)
    if es_primo(n):
        lista.append(n)
    return lista

def mcm(lista):
    """
    Devuelve el minimo comun multiplo de los numeros de la lista

    """
    mcm = 1
    for i in lista_primos(max(lista)):
        exp = 0
        for p in lista:
            exp = max(exp,lista_factores(p).count(i))
        mcm *= i ** exp
    return mcm       

def cant_divisores(n):
    """
    Devuelve el minimo comun multiplo de los numeros de la lista

    """
    cant = 1
    for i in lista_primos(n):
        exp = 0
        exp = max(exp,lista_factores(n).count(i))
        cant *= (exp + 1)
    return cant
     
        
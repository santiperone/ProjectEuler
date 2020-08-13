# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 11:22:41 2020

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
        print(i)
        cont = 0
        while residuo % i == 0:
            residuo = residuo / i
            cont += 1
            lista.append(i)
    if es_primo(n):
        lista.append(n)
    return lista

def factores_primos(n):
    lista = []
    residuo = n
    if es_primo(n):
        lista.append(n)   
        return lista
    for i in range(2,n//2+1):
        if es_primo(i):
            while residuo % i == 0:
                residuo = residuo / i
                lista.append(i)
    return lista

def D(n,m):
    suma = 0
    for i in lista_primos(max(n,m)):
        # print(i)
        expn = factores_primos(n).count(i)
        expm = factores_primos(m).count(i)
        # print(expn,expm)
        suma += abs(expn-expm)
    return suma 

def S(N):
    suma = 0
    for n in range(1,N+1):
        print(n)
        for m in range(1,N+1):
            suma += D(n,m)
    return suma
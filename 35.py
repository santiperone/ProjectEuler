# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 19:56:57 2020

@author: santi
"""
def es_primo(n):
    """
    Recibe un numero n y dice si es primo.

    """
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def lista_primos(n):
    lista = []
    for i in range(2,n+1):
        if es_primo(i):
            lista.append(i)
    return lista

def rotaciones(x):
    lista = []
    if len(x) <= 1:
        return x
    else:
        for i in range(len(x)):
            lista.append(x[i:] + x[:i])
    return(lista)

def es_circular(n):
    n = str(n)
    for i in rotaciones(n):
        i = int(i)
        if not es_primo(i):
            return False
    return True

def es_truncable(n):
    n = str(n)
    for i in range(1,len(n)):
        a = not es_primo(int(n[i:]))
        b = not es_primo(int(n[:i]))
        if a or b:
            return False
                                                   
from time import time
start =  time()
lista_primos = lista_primos(100)                   
                                           
### 6 DIGITOS
for a in [1,3,7,9]:
    for b in [1,3,7,9]:
        for c in [1,3,7,9]:
            for d in [1,3,7,9]:
                for e in [1,3,7,9]:
                    for f in [1,3,7,9]:
                        i = f  + 10*e + 100*d + 1000*c + 10000*b + 100000*a
                        if es_primo(i):
                            lista_primos.append(i)
### 5 DIGITOS
for a in [1,3,7,9]:
    for b in [1,3,7,9]:
        for c in [1,3,7,9]:
            for d in [1,3,7,9]:
                for e in [1,3,7,9]:
                    i = e + 10*d + 100*c + 1000*b + 10000*a
                    if es_primo(i):
                        lista_primos.append(i)
### 4 DIGITOS
for a in [1,3,7,9]:
    for b in [1,3,7,9]:
        for c in [1,3,7,9]:
            for d in [1,3,7,9]:
                i = d + 10*c + 100*b + 1000*a
                if es_primo(i):
                    lista_primos.append(i)                            
### 3 DIGITOS
for a in [1,3,7,9]:
    for b in [1,3,7,9]:
        for c in [1,3,7,9]:
            i = c + 10*b + 100*a
            if es_primo(i):
                lista_primos.append(i)                            
                            
lista = []       
for i in lista_primos:
    # if es_circular(i):
        # lista.append(i)
    if es_truncable(i):
        lista.append(i)
print(sum(lista))
print(time()-start)
                                          
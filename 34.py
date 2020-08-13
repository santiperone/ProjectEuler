# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 18:33:13 2020

@author: santi
"""

def factorial(n):
    if n == 0 or n ==1:
        return 1
    else:
        return n * factorial(n-1)

lista = []
for numero in range(11,99999):
    suma = 0
    for digito in str(numero):
        digito = int(digito)
        suma += factorial(digito)
    if suma == numero:
        lista.append(numero)
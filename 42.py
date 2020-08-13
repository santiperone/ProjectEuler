# -*- coding: utf-8 -*-
"""
Created on Sun May  3 02:51:05 2020

@author: santi
"""
def lista_triangular(n):
    lista = []
    for i in range(1,n+1):
        lista.append((i*(i+1))//2)
    return lista
    
listat = lista_triangular(1000)
f = open('p042_words.txt', 'r')
for word in f:
    f = word
lista = f.split('","')
lista[0] = 'A'
lista[1785] = 'YOUTH'

cont = 0
for word in lista:
    suma = 0
    for letter in word:
        suma += ord(letter) - 64
    if suma in listat:
        cont += 1

print(cont)



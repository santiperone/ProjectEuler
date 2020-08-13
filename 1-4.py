# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 20:33:21 2020

@author: santi
"""
## 1
suma = 0
for i in range(1,1000):
    if i % 3 == 0 or i % 5 == 0:
        suma += i
print(suma)

##2
def fibonacci(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)

def listaFibonacci(n):
    listafibonacci = []
    for i in range(0,n):
        listafibonacci.append(fibonacci(i))
    return listafibonacci

def sumevenfibonacci(n):
    suma = 0
    i = 0
    while fibonacci(i) <= n:
        if fibonacci(i) % 2 == 0:
            suma += fibonacci(i)
        i += 1
    return suma

##3
def es_primo(n):
    """
    Recibe un numero n y dice si es primo.

    """
    for i in range (2,int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def lista_divisores(n):
    """
    Recibe un numero n y devuelve una lista de sus divisores

    """ 
    lista = []
    for i in range(1,n):
        if n % i == 0:
            lista.append(i)
    return lista

def lista_primos(n):
    lista = []
    for i in range(1,int(n**0.5)+1):
        if es_primo(i):
            lista.append(i)
    return lista

for i in lista_primos(600851475143)[::-1]:
    if 600851475143 % i == 0:
        print(i)
        break

## 4
def largest_palindrome(n):
    lim_sup = 0
    for i in range(0,n):
        lim_sup += 9 * (10 ** i)
    lim_inf = lim_sup - 9 * (10 ** (n-1))
    # print(lim_inf)
    # print(lim_sup)
    largest = 0
    for i in range(lim_sup,lim_inf,-1):
        for p in range(lim_sup,lim_inf,-1):
            x = p * i
            x = str(x)
            if x == x[::-1]:
                largest = max(largest,int(x))
    return largest



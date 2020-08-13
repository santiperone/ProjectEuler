# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 17:40:40 2020

@author: santi
"""
def tri_num(n):
    return n*(n+1)//2

def cant_div(n):
    cont = 0
    for i in range(1,int(n/2)+1):
        if n % i == 0:
            cont += 1
    return cont

def cant_div_tri(n):
    if n % 2 == 0:
        cant = cant_div(n/2)*cant_div(n+1)
    else:
        cant = cant_div((n+1)/2)*cant_div(n)
    return cant

x = 1
while cant_div_tri(x) < 500:
    x += 1

print(tri(x))
    

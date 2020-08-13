# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 21:25:41 2020

@author: santi
"""

nmax  = 0
imax = 0
nimax = 0
for i in range(1,50000):
    funcionando = True
    n = 1
    num = ''
    while funcionando:
        # print(i)
        num += str(i*n)
        pandigital = True
        if num.count('0') > 0:
            funcionando = False
            pandigital = False      
        for j in range(1,10):
            if num.count(str(j)) > 1:
                funcionando = False
                pandigital = False
            elif  num.count(str(j)) == 0:
                pandigital = False
        if pandigital:
            nmax = max(int(num),nmax)
            nimax = n
            imax = i
            print(nmax)
            print(imax)
            print(nimax)
        n += 1

            
        
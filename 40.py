# -*- coding: utf-8 -*-
"""
Created on Sun May  3 02:44:52 2020

@author: santi
"""

x = ''
i = 1
while len(x) < 1000000:
    x += str(i)
    i += 1

exp = int(x[0]) * int(x[9]) * int(x[99]) * int(x[999]) * int(x[9999]) * int(x[99999]) * int(x[999999])
print(exp)

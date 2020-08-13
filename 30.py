# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 23:47:16 2020

@author: santi
"""

def prob30(x,n):
        s = 0
        for i in range(10,n):
                t = 0
                for a in str(i):
                        t += int(a)**x
                if t == i:
                        s += t
        return s
# prob30(5)

imax = 200000
imin = 0

while imin+1 < imax:
    if prob30(5,((imax+imin)//2)) == 443839:
        imax = (imax+imin)//2
        print(imax)
    else:
        imin = (imax+imin)//2
    # print(imin)
    # print(imax)
        
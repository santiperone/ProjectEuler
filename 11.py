# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 13:03:23 2020

@author: santi
"""
import numpy as np

x1 = '08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08'
x1 = x1.split()
x2 = '49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00'
x2 = x2.split()
x3 = '81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65'
x3 = x3.split()
x4 = '52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91'
x4 = x4.split()
x5 = '22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80'
x5 = x5.split()
x6 = '24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50'
x6 = x6.split()
x7 = '32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70'
x7 = x7.split()
x8 = '67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21'
x8 = x8.split()
x9 = '24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72'
x9 = x9.split()
x10 = '21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95'
x10 = x10.split()
x11 = '78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92'
x11 = x11.split()
x12 = '16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57'
x12 = x12.split()
x13 = '86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58'
x13 = x13.split()
x14 = '19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40'
x14 = x14.split()
x15 = '04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66'
x15 = x15.split()
x16 = '88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69'
x16 = x16.split()
x17 = '04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36'
x17 = x17.split()
x18 = '20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16'
x18 = x18.split()
x19 = '20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54'
x19 = x19.split()
x20 = '01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48'
x20 = x20.split()

x = np.array([x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15,x16,x17,x18,x19,x20])
x = x.astype(int)
prod = 0
for i in range(0,20):
    for j in range(0,17):
        a = 1
        # print(x[i][j:j+4])
        for k in range(j,j+4):
            a *= x[i,k]
        prod = max(prod,a)
        
for i in range(0,20):   # vertical adjacent
    for j in range(0,17):
        a = 1
        for k in range(j,j+4):
            a *= x[k,i]
        prod = max(prod,a)
        
for i in range(0,17):
    for j in range(0,17-i):
        a = 1
        for k in range(0,4):
            # print(x[i+j+k,j+k])
            a *= x[i+j+k,j+k]
        prod = max(prod,a)
        
for i in range(0,17):
    for j in range(0,17-i):
        a = 1
        for k in range(0,4):
            a *= x[j+k,i+j+k]
        prod = max(prod,a)
        
for i in range(3,20):
    # print()
    # print(i)
    for j in range(0,i-2):
        # print(j)
        a = 1
        for k in range(0,4):
            # print(x[j,19-j])
            a *= x[j+k,i-j-k]
        prod = max(prod,a)

for i in range(3,20):
    # print()
    # print(i)
    for j in range(0,i-2):
        # print(j)
        a = 1
        for k in range(0,4):
            # print(x[j,19-j])
            a *= x[j+k,i-j-k]
        prod = max(prod,a)
        


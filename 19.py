# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 14:01:23 2020

@author: santi
"""

dias = 0
domingos = 0
meses = ['enero','febero','marzo','abril','mayo','junio','julio',
         'agosto','septiembre','octubre','noviembre','diciembre']
m30 = ['abril','junio','noviembre','septiembre']
for año in range(1901,2001):
    for mes in meses:
        # print(mes)
        if mes == 'febrero':
            if año % 4:
                dias += 29
            else:
                dias += 28
        elif mes in m30:
            dias += 30
        else:
            dias += 31
        if dias % 7 == 5:
            domingos += 1

print(domingos)
                

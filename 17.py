# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 14:57:51 2020

@author: santi
"""

import inflect
ie = inflect.engine()

suma = 0
for i in range(1,1001):
    word = ie.number_to_words(i)
    word = word.translate({ord(c): None for c in ' -()%*!@#$'})
    suma += len(word)
    # print(word)
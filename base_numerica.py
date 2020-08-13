# -*- coding: utf-8 -*-
"""
Created on Sat May  2 21:05:35 2020

@author: santi
"""


class CrazySantiNumbers:   
    def __init__(self, digits=(1,)):
        self.digits = []
        for digit in digits:
            self.digits.append(str(digit))        
    def get_number(self, n):
          numeric_digits = []       
          num = n
          while num > 0:
              numeric_digits.append(num % len(self.digits))
              num //= len(self.digits)       
          out = ''
          for i in numeric_digits[::-1]:
              out += self.digits[i]          
          return out
      
prime = CrazySantiNumbers([1,3,7,9])
lista = []

for a in '2357':
    funcionando = True
    i = 1
    while funcionando:
        num = a + prime.get_number(i):
        if es_primo(num):
            i += 1
        else:
            funcionando = False
        
        
            
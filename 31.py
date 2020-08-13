# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 00:22:10 2020

@author: santi
"""
cont = 1
for l1 in range(2,-1,-1):      
        suma2 = l1*100
        for p50 in range((200-suma2)//50,-1,-1):
            suma3 = suma2+ 50*p50
            for p20 in range((200-suma3)//20,-1,-1):
                suma4 = suma3 + 20*p20
                for p10 in range((200-suma4)//10,-1,-1):
                    suma5 = suma4 + 10*p10
                    for p5 in range((200-suma5)//5,-1,-1):
                        suma6 = suma5 + 5*p5
                        for p2 in range((200-suma6)//2,-1,-1):
                            suma7 = suma6 + 2*p2
                            for p1 in range((200-suma7),-1,-1):
                                    if suma7 + p1 == 200:
                                        cont+=1
                                        # print(l2)
                                        # print(l1)
                                        # print(p50)
                                        # print(p20)
                                        # print(p10)
                                        # print(p5)
                                        # print(p2)
                                        # print()
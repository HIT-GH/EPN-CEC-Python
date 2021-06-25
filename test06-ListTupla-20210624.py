# -*- coding: utf-8 -*-
"""
Created on Thu Jun 24 19:47:07 2021

@author: HendersonIturralde
"""

lista1 = ["Juan",5,5.7,True,5,"no"]
print(type(lista1))
print(len(lista1),"\n")
tupla1 = ("Juan",5,5.7,True,5,False,"Pedro")
print(type(tupla1))
print(len(tupla1),"\n")

print(lista1[0])
print(lista1[1])
print(lista1[2])
print(lista1[-1])
print(lista1[-5],"\n")

print(tupla1[0])
print(tupla1[1])
print(tupla1[2])
print(tupla1[-1])
print(tupla1[-5],"\n")

lista1[1] = "Carlos"
print(lista1)

#tupla1[0] = "R2"
print(tupla1)

del lista1[2]
del tupla1[0]
print(lista1)
print(tupla1)

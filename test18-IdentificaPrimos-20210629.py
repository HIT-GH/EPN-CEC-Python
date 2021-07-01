# -*- coding: utf-8 -*-
"""
Created on Tue Jun 29 18:25:03 2021

@author: HendersonIturralde
"""

x = 7
restos=[]

for item in range (2,x):
    resto=x%item
    print(resto)
    restos.append(resto)

print(restos)

if 0 in restos:
    print("No es primo\n")
else:
    print("Es primo\n")



is_prime=True
for item in range (2,x):
    resto=x%item
    if resto==0:
        is_prime=False
        print("No es primo")
        break

if is_prime==True:
    print("Es primo")
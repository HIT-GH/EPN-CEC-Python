# -*- coding: utf-8 -*-
"""
Created on Tue Jun 29 18:57:07 2021
@author: HendersonIturralde
"""

x = int(input("Ingrese el valor a comprobar: "))
y = 2

while y < x:
    is_prime=True    
    for item in range (2,y):
        resto=y%item
        if resto==0:
            is_prime=False
            print("No es primo")
            break

    if is_prime==True:
        print("Es primo > ", y)
        
    y += 1


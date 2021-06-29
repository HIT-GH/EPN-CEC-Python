# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 19:15:36 2021
@author: HendersonIturralde
"""

print("--------    Without Functions    --------\n")

print("Ingrese un valor: ")
a = input()
print("Ingrese un valor: ")
b = input()
print("Ingrese un valor: ")
c = input()

print(a,b,c)


print("--------    With Functions    --------\n")

def mensaje():
    print("Por favor, ingrese un valor: ")
    
print("Inicio")
mensaje()
d = input()
mensaje()
e = input()
mensaje()
f = input()

print(d, e, f)

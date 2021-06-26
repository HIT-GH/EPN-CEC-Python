# -*- coding: utf-8 -*-
"""
Created on Fri Jun 25 18:24:28 2021
@author: HendersonIturralde
"""

print("Por favor, ingrese los siguientes datos:")
fname = input("  Nombre:    ")
lname = input("  Apellido:  ")
location = input("  Ubicación: ")
age = int(input("  Edad:      "))
space = " "

print("")
print("¡Bienvenido" + space + fname + space + lname + "!")
print("Su edad es", age, "años.")
print("Usted se encuentra en" + space + location + ".")
print("Esperamos que disfrute su estadía.")


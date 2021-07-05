# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 20:24:13 2021
@author: HendersonIturralde
"""

def validar_numero(prompt, min, max):
    while (True):
        try:
            print("Ingrese un valor entre", min, "y", max)
            x = int(input(prompt))
            assert x >= min and x <= max
            return x
        
        except ValueError:
            print("Error: Ingresar solo números")
        except:
            print("Error: el valor debe estar dentro del rango")

v = validar_numero("Ingrese un valore en el rango a", -100, 100)

print("El número es: ", v)
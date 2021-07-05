# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 19:30:20 2021
@author: HendersonIturralde
"""

#   Manejo de errores

print("Inicio")
try:
    x = int(input("Ingrese un número: "))
    y = 1/x
    print(y)
except ArithmeticError:
    print("Error Aritmético General")
except ZeroDivisionError:
    print("Error: división para 0")
except ValueError:
    print("Error: debe ingresar un número")
except:
    print("Error no reconocido")

print("Fin")

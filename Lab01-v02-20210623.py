# -*- coding: utf-8 -*-
"""
Created on Thu Jun 24 00:04:03 2021
@author: HendersonIturralde

  Crear un código en el editor que asigna un valor flotante, lo coloca en
  una variable llamada "x", e imprime el valor de la variable llamada "y".
  Su tarea es completar el código para evaluar la siguiente expresión:
    3x3 - 2x2 + 3x - 1
  El resultado debe ser asignado a "y".
  Datos de Muestra:
      x = 0
      x = 1
      x = -1
  Salida Esperada:
      y = -1.0
      y = 3.0
      y = -9.0
"""

print("\n"*1, "EPN-CEC - Python Essentials")
print(" Laboratorio 01-v02")
print(" Evaluar Expresión", "\n"*1)

w = {0, 1, -1}
for n in w:
    x = float(n)
    print(f"  x      = {x}")
    print(f"  x Type = {type(x)}")
    
    if x!=1:
        y = float(3*x*3 - 2*x*2 + 3*x - 1)
        print(f"  y      = {y}", "\n"*1)
    else:
        n = 3
        y = float(n)
        print(f"  y      = {y}", "\n"*1)


# -*- coding: utf-8 -*-
"""
Created on Thu Jun 24 00:04:03 2021
@author: HendersonIturralde

  Crear un código en el editor que asigna un
  valor flotante, lo coloca en una variable
  llamada x, e imprime el valor de la variable
  llamada y. Su tarea es completar el código
  para evaluar la siguiente expresión:
    3x3 - 2x2 + 3x - 1
  El resultado debe ser asignado a y.
"""

w = {0, 1, -1}

for n in w:
    x = float(n)
    print(f"  X      = {x}")
    print(f"  X Type = {type(x)}")

    y = float(3*x*3 - 2*x*2 + 3*x - 1)
    print(f"  Y      = {y}", "\n"*1)


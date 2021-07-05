# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 20:09:42 2021
@author: HendersonIturralde
"""

def read_range(prompt, min, max):
    try:
        in_ok = False
        while in_ok == False:
            print(prompt, "en el rango", min, "a", max)
            in_value = int(input("Valor: "))
            if in_value<min or in_value>max:
                print("Error - Número fuera de rango")
            else:
                print("Ingreso correcto:", in_value)
                in_ok = True

    except ValueError:
        print("Error: debe ingresar un número")
        

read_range("Ingrese un entero", -5, 20)


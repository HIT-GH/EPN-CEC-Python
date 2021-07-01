# -*- coding: utf-8 -*-
"""
Created on Wed Jun 30 18:52:30 2021
@author: HendersonIturralde
"""

#--------------------------------------------------------------
#   TAREA FUNCIONES 2.1 / 2021.06.30
#   Escribir una función que toma un año y devuelve Verdadero
#   si dicho año es bisiesto o Falso de lo contrario.
#
#   Ref:
#    - Año bisiesto es aquel divisible para 4.
#    - Año divisible para 100 es bisiesto si también es
#      divisible para 400.
#--------------------------------------------------------------

test_data = [1900, 2000, 2016, 1987, 1908, 1970]


#---    Fun Year Leap    --------------------------------------

def is_year_leap(year):
    year_leap = False
    
    if (year%100 != 0) and (year%4 == 0):
        year_leap = True
    elif (year%100 == 0) and (year%400 == 0):
        year_leap = True
        
    return year_leap


#---    Test    -----------------------------------------------

test_results = []
for item in test_data:
    test_results.append(is_year_leap(item))

print("\n----------  Cálculo Año Bisiesto  ----------\n")
print(f" Datos de Prueba: {test_data}")
print(f" Resultados:      {test_results}")



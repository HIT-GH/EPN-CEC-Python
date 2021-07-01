# -*- coding: utf-8 -*-
"""
Created on Wed Jun 30 18:52:30 2021
@author: HendersonIturralde
"""

#--------------------------------------------------------------
#   TAREA FUNCIONES 2.2 / 2021.06.30
#   Escribir una función que toma dos argumentos (un año y un 
#   mes) y devuelve el número de días para el par mes-año dado. 
#   Aunque solo febrero es sensible al valor del año, la función 
#   deberá ser universal.
#
#   Ref:
#    - Año bisiesto es aquel divisible para 4.
#    - Año divisible para 100 es bisiesto si también es
#      divisible para 400.
#--------------------------------------------------------------

test_years  = [1900, 2000, 2016, 1987, 1908, 1970]
test_months = [2, 2, 1, 11, 2, 8]

data_days  = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

#---    Fun Year Leap    --------------------------------------

def is_year_leap(year):
    year_leap = False
    
    if (year%100 != 0) and (year%4 == 0):
        year_leap = True
    elif (year%100 == 0) and (year%400 == 0):
        year_leap = True
        
    return year_leap


#---    Fun Days in Month    ----------------------------------

def days_in_month(year, month):
    if (month == 2) and (is_year_leap(year) == True):
        return 29
    else:
        return data_days[month-1]


#---    Test    -----------------------------------------------

test_results = []
for item in range(len(test_years)):
    test_results.append(days_in_month(test_years[item], test_months[item]))

print("\n----------  Cálculo Días en Años-Mes  ----------\n")
print(f" Año:         {test_years}")
print(f" Mes:         {test_months}")
print(f" Resultados:  {test_results}")


####    EoF    ################################################

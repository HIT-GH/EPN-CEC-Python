# -*- coding: utf-8 -*-
"""
Created on Wed Jun 30 18:52:30 2021
@author: HendersonIturralde
"""

"""
---------------------------------------------------------------
    TAREA FUNCIONES 2.3 / 2021.07.04
    Escribir una función que toma tres argumentos (un año, un
    mes y un día del mes) y devuelve el día correspondiente del
    año, o devuelve None si alguno de los argumentos es inválido.
    Agregue casos de prueba al código. 

    Ref:
    - Año bisiesto es aquel divisible para 4.
    - Año divisible para 100 es bisiesto si también es
      divisible para 400.
    - Días por mes:
      En  Fe  Mr  Ab  My  Jn  Jl  Ag  Sp  Oc  Nv  Dc
      31  28*31  30  31  30  31  31  30  31  30  31
      (*) 29 en año bisiesto
---------------------------------------------------------------
"""

data_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

#---    Funct Year Leap    ------------------------------------

def is_year_leap(year):
    year_leap = False
    
    if (year%100 != 0) and (year%4 == 0):
        year_leap = True
    elif (year%100 == 0) and (year%400 == 0):
        year_leap = True
        
    return year_leap


#---    Funct Days in Month    --------------------------------

def days_in_month(year, month):
    if (month == 2) and (is_year_leap(year) == True):
        return 29
    else:
        return data_days[month-1]


#---    Funct Valid Date (Month & Day)   ----------------------

def valid_date(year, month, day):
    if (month < 1) or (month > 12) or (day < 1):
        return False
    elif (month == 2) and is_year_leap(year):
        if day > 29:
            return False
        else:
            return True
    elif (day > data_days[month]):
        return False
    else:
        return True
    

#---    Test    -----------------------------------------------

t_y  = [1900, 2000, 2016, 1987, 2021, 2020]
t_m  = [2, 2, 10, 11, 7, 1]
t_d  = [15, 28, 17, 4, 4, 32]

print("\n----------  Cálculo Número del Día en el Año  ----------")
print("       Fechas expresadas en el formato YYYY.MM.DD\n")

cntr = 0
for item in t_y:
    print(f"Prueba {cntr+1} - fecha: {t_y[cntr]}.{t_m[cntr]}.{t_d[cntr]}")

    if valid_date(t_y[cntr], t_m[cntr], t_d[cntr]):

        if is_year_leap(t_y[cntr]):
            yl_txt = "Este año es bisiesto."
            if t_m[cntr] >2:
                total_days = t_d[cntr] + 1
            else:
                total_days = t_d[cntr]
        else:
            yl_txt = "Este año es NO bisiesto."
            total_days = t_d[cntr]

        for item in range(t_m[cntr]):
            total_days = total_days + data_days[item]

        print(f"    {yl_txt}")
        print(f"    La fecha {t_y[cntr]}.{t_m[cntr]}.{t_d[cntr]} corresponde")
        print(f"    al día {total_days} del año {t_y[cntr]}.\n")
    else:
        print("    ERROR: Fecha inválida.")
        print("    El valor del mes o día están fuera de rango.")

    cntr += 1


####    EoF    ################################################

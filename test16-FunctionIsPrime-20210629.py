# -*- coding: utf-8 -*-
"""
Created on Tue Jun 29 18:14:28 2021
@author: HendersonIturralde
"""

print("")
print("≡-≡-≡-≡    Generador de Números Primos    ≡-≡-≡-≡")


#---    fun: GENERADOR DE NÚMEROS PRIMOS    -------------------
def generador_primos(x):
    y = 2
    
    while y < x:
        is_prime = True
        
        for item in range (2,y):
            resto = y % item
            if resto==0:
                is_prime = False
                break
        
        if is_prime==True:
            print("  ", y)
            
        y += 1
#---    End Fun: GENERADOR DE NÚMEROS PRIMOS    ---------------

seguir = "S"
while seguir == "S":
    max_val = int(input("Ingrese el valor mayor a 2 para comprobar: "))
    print("Los primos entre 1 y", max_val, "son:")
    generador_primos(max_val+1)
    seguir = (input('Presione "S" si quiere generar otra cadena: ')).upper()
    

#---    EoF    ------------------------------------------------

# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 18:45:04 2021

@author: HendersonIturralde
"""

print("--------    While in a While    --------\n")
counter = 0
while True:
    counter += 1
    print("\n Ejecución # ", counter)
    x = input('Ingrese máxima cuenta o "Q" para salir: ')
    if x == 'q' or x == 'Q':
        print ("Breaking 01 - Full process")
        break
    
    x = int(x)
    y = 1
    while True:
        print(y)
        y = y+1
        if y>x:
            print ("Breaking 02 - Counter process")
            break


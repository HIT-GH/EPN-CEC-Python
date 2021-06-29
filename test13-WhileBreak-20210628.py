# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 18:31:32 2021
@author: HendersonIturralde
"""

print("--------    While & Break    --------\n")
max_val = input("Ingrese el número total: ")
max_val = int(max_val)
counter = 0

print("counter =", counter)
print("max count value =", max_val, "\n")
print("Before while.")
while True:
    print("    counter = ", counter, "  (inside While)")
    counter += 1
    if counter>max_val:
        break
    input("    press any key to continue...")

print("After while.")

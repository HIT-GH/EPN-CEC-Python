# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 18:20:50 2021
@author: HendersonIturralde
"""

max_val = input("Ingrese el número total: ")
max_val = int(max_val)
counter = 0

print("Before while.")
while counter <= max_val:
    print("    counter = ", counter, "  (inside While)")
    counter += 1
    input("    press any key to continue...")

print("After while.")
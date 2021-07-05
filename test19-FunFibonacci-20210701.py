# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 18:09:49 2021
@author: HendersonIturralde
"""



def fibonacci(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    
    print()


print(fibonacci(5))
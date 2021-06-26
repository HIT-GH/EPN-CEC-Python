# -*- coding: utf-8 -*-
"""
Created on Fri Jun 25 19:26:32 2021
@author: HendersonIturralde
"""

Datos = int(input("Ingrese VLAN de Datos:  "))
Nativa = int(input("Ingrese VLAN Nativa:    "))
print("")

#Datos = 1000
#Nativa = 1

if Datos==Nativa:
    print("  >>  Las VLANs son iguales.")
else:
    print("  >>  Las VLANs son diferentes.")
    
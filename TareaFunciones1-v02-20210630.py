# -*- coding: utf-8 -*-
"""
Created on Wed Jun 30 18:52:30 2021
@author: HendersonIturralde
"""

#--------------------------------------------------------------
#   TAREA FUNCIONES 1 / 2021.06.30
#   Escribir dos funciones que conviertan:
#     Fun 1. l100kmtompg - Lts/100km a MPG (Millas por Galón)
#     Fun 2. mpgtol100km - MPG (Millas por Galón) a Lts/100km
#
#   Refs:
#     1 milla americana = 1609.344 metros
#     1 galón americano = 3.785411784 litros.
#--------------------------------------------------------------

list_ltom = [3.9, 7.5, 10.0]
list_mtol = [60.3, 31.4, 23.5]


#---   Fun 1. Lts/100km a MPG    ------------------------------
#   lpkm = lphkm/100
#   lpm  = lpkm*1.609344
#   gpm  = lpm/3.785411784
#   mpg  = 1/gpm

def l100kmtompg(lphkm):
    return 1/(((lphkm/100)*1.609344)/3.785411784)


#---    Fun 2. MPG a Lts/100km    -----------------------------
#   kpg   = mpg*1.609344
#   kpl   = kpg/3.785411784
#   lpkm  = 1/kpl
#   lphkm = lpkm*100

def mpgtol100km(mpg):
    return (1/((mpg*1.609344)/3.785411784))*100


#---    Test    -----------------------------------------------

print("Conversión entre representaciones de Consumo de Combustible")
print("\n Lts/100km to MPG:")
for item in list_ltom:
    print(f"   {item} lts/100Km = {l100kmtompg(item)} MPG")
    
print("\n MPG to Lts/100km:")
for item in list_mtol:
    print(f"   {item} MPG = {mpgtol100km(item)} lts/100Km")

    
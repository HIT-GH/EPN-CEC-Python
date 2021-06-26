# -*- coding: utf-8 -*-
"""
Created on Fri Jun 25 19:42:27 2021
@author: HendersonIturralde
"""

acl=int(input("Ingrese el # de ACL: "))

if acl >= 1 and acl <= 99:
    print("  >>  La ACL es Estándar.")
elif acl >= 100 and acl <= 199:
    print("  >>  La ACL es Extendida.")
else:
    print("  >>  El # ingresado no es de ACL IPv4")


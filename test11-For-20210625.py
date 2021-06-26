# -*- coding: utf-8 -*-
"""
Created on Fri Jun 25 19:58:55 2021
@author: HendersonIturralde
"""

MyList = ["RT-01", "RT-02", "AP-03",
          "AP-01", "SW-02", "SW-03",
          "SW-01", "AP-02", "RT-03"]

print("\n  ---»  My List =", MyList)
print("  ---»  The length of My List =", len(MyList), "\n")

#---  FOR  ----------------------------------------------------

print("::::::::    JUST FOR    ::::::::")
print("\n", "Before FOR")
for item in MyList:
    print("  ", item, " >  Inside FOR")

print(" After FOR", "\n"*2)


#---  FOR & Conditions  ---------------------------------------

print("::::::::    FOR + CONDITION    ::::::::")
print("\n", "Before FOR")
for item in MyList:
    if "RT" in item:
        print("  ", item, " >  Inside FOR")

print(" After FOR", "\n"*2)


#---  Append RTs  ---------------------------------------------
MyNewList = []

print("::::::::    FOR + CONDITION + APPEND   ::::::::")
print("\n", "Before FOR")
for item in MyList:
    if "RT" in item:
        print("  ", item, " >  Inside FOR")
        MyNewList.append(item)

print(" After FOR", "\n")
print(MyNewList, "\n"*2)


#---  Append RTs, SWs and APs  --------------------------------
MyNewListRT = []
MyNewListSW = []
MyNewListAP = []

print("::::::::    FOR + CONDITIONS + APPEND   ::::::::")
print("\n", "Before FOR")
counter = 0
for item in MyList:
    print("   Working on item", counter)
    counter += 1
    if "RT" in item:
        MyNewListRT.append(item)
    elif "SW" in item:
        MyNewListSW.append(item)
    else:
        MyNewListAP.append(item)

print(" After FOR", "\n")
print("My RT List =", MyNewListRT)
print("My SW List =", MyNewListSW)
print("My AP List =", MyNewListAP)


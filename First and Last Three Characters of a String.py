# -*- coding: utf-8 -*-
"""
Created on Sun Sep 10 23:28:39 2023

@author: USER
"""

s = input("Enter the string : ")

if len(s)<6:
    print("")
else:
    print("New string is ",s[:3]+s[len(s)-3:])

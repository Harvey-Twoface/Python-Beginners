# -*- coding: utf-8 -*-
"""
Created on Sun Sep 10 23:04:53 2023

@author: USER
"""

s = input("Enter the string : ")

i = int(input('Enter the index : '))    

try: 
    if len(s)==0:
        raise Exception("Empty String")
    elif i>=len(s) or i<0:
        raise Exception("i is out of range")
    else: 
        print(f"The indexed element of {s} is {s[i]}")
except Exception as e:
    print(str(e))
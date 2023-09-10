# -*- coding: utf-8 -*-
"""
Created on Sun Sep 10 23:53:03 2023

@author: USER
"""

s = input("Enter the string : ")
new=""
if len(s)==0 or len(s)==1:
    print(s)
for i in range(0,len(s)):
    if i%2!=0:
        new+=s[i]
        #print(new)
print(f"{s} without the characters located at even indices is {new}.")

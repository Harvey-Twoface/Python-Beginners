""" Write a Python program that prints a version of the string s with all commas replaced by dots. """

"""
s = input("Enter the string : ")

s = s.replace(",",".")
print("The new string is ",s) """

#OR

s = input("Enter the string : ")

comma =","
dot="."

new=""

for i in s:
    if i==comma:
        new+=dot
    else:
        new+=i
print('The new string is ',new)        
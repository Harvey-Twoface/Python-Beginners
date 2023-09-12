"""
Write a Python program that prints a copy of the string s without any spaces.

Words should be connected in the final string.

If the string doesn't contain spaces, print it intact.
 
"""
s = input("Enter the string : ")
space = " "
new=""
for i in s:
    if i!=space:
        new+=i

if space in s:    
    print(new)
else:
    print(s)
        

""" 
Write a Python program that reverses the individual words in the string s and changes their capitalization. Uppercase letters should be printed in lowercase and vice versa.

Assume that the string only contains letters and spaces are used to separate words.

"""
s = input("Enter a string : ")
new=""
for i in s:
    if i.isupper():
        new+=i.lower()
    else:
        new+=i.upper()
words = new.split()
print(words)

reverseds = " ".join(word[::-1] for word in words)

print(reverseds)
    

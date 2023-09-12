""" 
Write a Python program that checks if the string s ends with a specific sequence of characters denoted by the variable suffix.

If it does, print True. Else, print False.

This test should be case sensitive. Therefore, "A" should not be equivalent to "a".

If the length of the suffix is greater than the length of the string, print False.

"""
s = input("Enter the string : ")
suffix = input("Enter the prefix : ")

if len(suffix)>len(s):
    print(False)
else:
    if s[-len(suffix):]==suffix:
        print(True)
    else:
        print(False)

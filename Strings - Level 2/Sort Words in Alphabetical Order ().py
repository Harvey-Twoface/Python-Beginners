"""
Write a Python program to convert a string s to lowercase, sort the characters of each word in alphabetical order, and print the resulting string.

You may assume that the string only contains letters and spaces to separate the words.

Spaces should be preserved in the final string.

"""

s = input("Enter a string : ")
new=""
for i in s:
    if i.isupper():
        new+=i.lower()
    else:
        new+=i
word = new.split()

sorted_words = ["".join(sorted(words)) for words in word]

sorted_string = ' '.join(i for i in sorted_words)

print(f"The letter of the strings sorted in alphabetical order is : {sorted_string}")
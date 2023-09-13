"""
Write a Python program to count the number of repeated characters in the string s.

The program must print the total number of repeated characters and a message on the next line displaying the repeated characters separated by a space and sorted alphabetically.

If there are no repeated characters in the string, print 0 as the total count and None on the next line
"""

s = input("Enter the string : ")

count=0
char=""
chars=[]
for i in s:
    if i in char:
        char+=i
        count+=1
        chars.append(i)
    else:
        char+=i
letters = " ".join(word for word in chars)
if count==0:
    print("None")
else:
    print(f"count: {count} and the letters : {letters}")

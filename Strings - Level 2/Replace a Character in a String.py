""" Write a Python program that prints the string s with the character curr_char replaced by the character new_char.

curr_char and new_char are variables that contain strings with a single character.

You may assume that new_char will not be an empty string.

The match must be case-sensitive (do not replace lowercase letters if curr_char is uppercase).

If no match is found, print the initial string. """


s = input("Enter the string : ")

curr_char = input("Enter the character currentcharacter : ")
new_char = input("Enter the character new character : ")

if len(new_char)==0:
    print("New character cannot be empty")
else:
    for i in range(len(s)):
        if s[i]==curr_char:
            #print(s[i])
            s=s.replace(s[i],new_char)
print("The string is",s)

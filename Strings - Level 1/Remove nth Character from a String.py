s = input("Enter the string : ")
n = int(input("Enter the index: "))
new=""

if n>=len(s) or len(s)==0:
    print(s)
else:
    for i in range (0,len(s)):
        if i!=n:
            new+=s[i]
           
    print(new)
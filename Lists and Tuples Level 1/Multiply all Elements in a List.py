"""
Write a Python program that multiplies all the items in a list by the value of the variable factor.

The program must print the list as the output.

The program should also allow multiplying the variable factor by a string in case the list contains strings.

You may assume that the value of factor will be a positive integer.

"""
#integer
size = int(input("Enter the size of the list size : "))
l = []

for i in range(size):
    n = int(input("Enter the element : "))
    l.append(n)
print("The list is : ",l)
factor = int(input("Enter the factor : "))    

for i,elem in enumerate(l):
    l[i]=elem*factor

print("The updated list is : ",l)

#string 
    
size2 = int(input("Enter the size of the list size : "))
l2 = []
for i in range(size2):
    n2 = input("Enter the element : ")
    l2.append(n2)
print("The list is : ",l2)

factor2 = int(input("Enter the factor : "))    

for i in range(len(l2)):
    l2[i]*=factor2

print("The updated list is : ",l2)    
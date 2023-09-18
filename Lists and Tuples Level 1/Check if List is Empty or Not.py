"""
Write a Python program that checks if a list is empty or not.

If the list is empty, print "Empty". Else, print "Not Empty".

"""
size = int(input("Enter the size of the list: "))
l =[]
for i in range(size):
    e = int(input("enter the element: "))
    l.append(e)
    
if l:
    print("Not Empty")
else:
    print("Empty")
"""
Write a Python program that prints the elements of a list followed their corresponding indices.

Each element and its index must be on the same line separated by a space.

If the list is empty, print "Empty List".

"""

size = int(input("Enter the size of the list: "))
l =[]
for i in range(size):
    e = input("enter the element: ")
    if e.isdigit():
        e=int(e)
        l.append(e)
    else:
        l.append(e)

if l:    
    for k,elem in enumerate(l):
        print(elem,k)
else:
    print("Empty List")
    
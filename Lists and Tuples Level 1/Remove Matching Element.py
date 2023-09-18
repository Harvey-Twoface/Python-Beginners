"""
Write a Python program that removes all occurrences of the element elem_to_remove from a list.

The output of the program should be the new list with the element removed.

If the element is not found in the list, print the message "Not Found".

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
        
elem_to_remove = input("enter the element to remove: ")
if elem_to_remove.isdigit():
    elem_to_remove=int(elem_to_remove)
if l:
    if elem_to_remove in l:
        for k in l:
            if elem_to_remove==k:
                l.remove(elem_to_remove)
        print("Updated list : ",l)
    
    else:
        print("Not found")
    
else:
    print("Empty List")
    
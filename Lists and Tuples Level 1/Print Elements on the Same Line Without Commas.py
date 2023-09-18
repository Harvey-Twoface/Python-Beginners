"""
Write a Python program that prints the elements of a list on the same line.

The elements should be separated only by a space (not by a comma).

The output should not include the opening and closing square brackets [ ].

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

print("The list : ",l)

new = " ".join(str(element) for element in l)

print("The output is : ", new)
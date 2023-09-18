size = int(input("Enter the size of the list: "))
l =[]
for i in range(size):
    e = int(input("enter the element: "))
    l.append(e)
    
print("The list is :",l)

if l:
    print(max(l),min(l))



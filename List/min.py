mylist=[]
n=int(input("Enter the number of elements: "))
for i in range(1,n+1):
    get=int(input("Enter %d element: "%i))
    mylist.append(get)
min=mylist[0]
for i in mylist:
    if i<min:
        min=i
print(min)

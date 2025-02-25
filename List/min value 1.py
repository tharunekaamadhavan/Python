mylist=[]

n=int(input("Enter number of elements in the list: "))
for i in range(1,n+1):
    lis=int(input("Enter %d element: "%i))
    mylist.append(lis)
min=mylist[0]
for i in mylist:
    if i<min:
        min=i
print(min)

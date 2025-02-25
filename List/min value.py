mylist=[]

n=int(input("Enter number of elements in the list: "))
for i in range(1,n+1):
    lis=int(input("Enter %d element: "%i))
    mylist.append(lis)

for i in range(len(mylist)-1):
    if mylist[i]>mylist[i+1]:
        print(mylist[i+1])
        
            

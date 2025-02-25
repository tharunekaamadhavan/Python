mylist=[]
n=int(input("Enter the number of elements: "))
for i in range(1,n+1):
    get=int(input("Enter %d element: "%i))
    mylist.append(get)
result=[]
for i in mylist:
    if i%5==0:
        result.append(i)
a=tuple(result)
print(a)
        

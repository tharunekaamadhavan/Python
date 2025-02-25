n=int(input("no of elements: "))
mylist=[]
for i in range(1,n+1):
    data=int(input("enter %d element: "%i))
    mylist.append(data)
result_list=[]
for value in mylist:
    count=0
    for i in mylist:
        if value==i:
            count=count+1
    if count==1:
        result_list.append(value)
print(result_list)

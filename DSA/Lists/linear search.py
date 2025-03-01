mylist=[1,2,6,5,12,9,45,10]
n=len(mylist)
i=0
key=int(input("Enter an element to search: "))
while(i<n):
    if(key==mylist[i]):
        print("Key found at ",i+1)
        break
    i=i+1
else:
    print("Key not found")

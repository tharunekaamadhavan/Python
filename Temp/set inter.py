n=int(input("Enter the number of elements of set 1: "))
set1=set()
for i in range(1,n+1):
    sett1=int(input("Enter %d element: "%i))
    set1.add(sett1)
m=int(input("Enter the number of elements of set 2: "))
set2=set()
for i in range(1,n+1):
    sett2=int(input("Enter %d element: "%i))
    set2.add(sett2)
final=set1.intersection(set2)
print(final)

    

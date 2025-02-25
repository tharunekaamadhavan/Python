n=int(input("Enter number of elements: "))
d=[]
for i in range(1,n+1):
    data=int(input("Enter %d element: "%i))
    d.append(data)
print(d)
s=int(input("Enter search element: "))
i=0
while i<len(d):
    if d[i]==s:
        print("Element found")
        break
    i=i+1
else:
    print("Element not found")

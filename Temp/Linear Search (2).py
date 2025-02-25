li=[32,6524,6,35,7678,553,53,68,4,567,2,6]
key=int(input("Enter the element to be searched:"))
i=0
while i<len(li):
    if key==li[i]:
        print("Element found")
        break
    i+=1
else:
    print("Element not found")

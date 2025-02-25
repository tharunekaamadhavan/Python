def bub(arr):
    for i in range(len(arr)):
        swapped=False
        for j in range(len(arr)-i-1):
            
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                swapped=True
        if swapped==False:
            break
arr=[64,34,25,12,22,11,90]
bub(arr)
print("Sorted list:",arr)

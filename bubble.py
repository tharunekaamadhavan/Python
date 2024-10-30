def bubble(arr):
    for i in range(len(arr)):
        swapped=False
        for j in range(len(arr)-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                swapped=True
arr=[43,6,25,6,4,78,3]
bubble(arr)
print(arr)
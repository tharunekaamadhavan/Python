def quick(arr):
    if len(arr)<=1:
        return arr
    else:
        pivot=arr[0]
        left=[x for x in arr[1:] if x<pivot]
        right=[x for x in arr[1:] if x>=pivot]
        return quick(left)+[pivot]+quick(right)
arr=[5,1,8,3,2]
y=quick(arr)
print("Sorted array:",y)

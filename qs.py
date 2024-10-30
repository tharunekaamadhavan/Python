def quick(arr):
    if len(arr)<=1:
        return arr
    else:
        pivot=arr[0]
        left=[x for x in arr[1:] if x<pivot]
        right=[x for x in arr[1:]if x>pivot]
        return quick(left)+[pivot]+quick(right)
arr=[6,3,6,7,2,6,7,4,6,7]
sor=quick(arr)
print(sor)
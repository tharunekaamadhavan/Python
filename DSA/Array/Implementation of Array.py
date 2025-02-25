from array import *
print("Array Implementation")
ch=int(input("Choices:\n1.Sort\n2.Reverse\n3.Append\nEnter your choice:"))
arr=array('i',[1,9,5,6])
if ch==1:
    print("Sorted array:",sorted(arr))
elif ch==2:
    arr.reverse()
    print("Reversed array:",arr)
elif ch==3:
    a=int(input("Enter element to be appended:"))
    arr.append(a)
    print("Append list:",arr)
else:
    print("Invalid choice")
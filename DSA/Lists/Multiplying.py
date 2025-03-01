def fun(a):
    for i in range(len(a)):
        a[i]=a[i]*5
list1=[1,2,3,4,5]
print("list before calling function: ",list1)
fun(list1)
print("list after calling function: ",list1)

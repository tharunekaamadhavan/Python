n=int(input())
arr=map(int,input().split())
a=list(arr)
arr1=[]
for i in range(len(a)):
    for j in range(1,len(a)):
        if a[i]<a[j]:
            a.append(j)
for i in range(len(arr1)):
    if arr1[i]<a[i+1]:
        print(arr1[i+1])

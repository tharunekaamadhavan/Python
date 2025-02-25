def selectionsort(n):
    for i in range(len(a)):
        mini=i
        for j in range(i+1,len(a)):
            if a[j]<a[mini]:
                mini=j
            temp=a[i]
            a[i]=a[mini]
            a[mini]=temp
    print(a)
a=[4,3,0,2]
selectionsort(a)

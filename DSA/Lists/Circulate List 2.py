def circulate(listt,n):
    i=1
    while i<=n:
        j=len(listt)-1
        while j>0:
            temp=listt[j]
            listt[j]=listt[j-1]
            listt[j-1]=temp
            j=j-1
        print("rotation", i, listt)
        i=i+1
    return
listt=[1,2,3,4,5]
circulate(listt,4)

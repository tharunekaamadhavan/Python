
def circulate(lol,numofrot):
    i=1
    while i<numofrot:
        a=len(lol)-1
        while a>0:
            temp=lol[a]
            lol[a]=lol[a-1]
            lol[a-1]=temp
            
            a=a-1
        print("rotation",i,lol)
        i=i+1
    return
lol=[1,2,3,4,5]
circulate(lol,5)
    

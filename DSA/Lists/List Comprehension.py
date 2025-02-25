x=1
y=1
z=2
n=3

print("Without list comprehension")
li=[]
for i in range(x+1):
    for j in range(y+1):
        for k in range(z+1):
            l=[i,j,k]
            li.append(l)
print(li)
lis=[]
for i in li:
    s=0
    for j in range(len(i)):
        s+=i[j]
    if s!=n:
        lis.append(i)
print(lis)

print("With list comprehension")
listt=[[i,j,k]for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k!=3]
print(listt)
            

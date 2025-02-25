n=int(input("Enter n: "))
for i in range(1,n+1):
    for j in range(i):
        print("*",end="")
    print()


n=int(input("Enter n: "))
for i in range(n,0,-1):
    for j in range(i):
        print("*",end="")
    print()


n=int(input("Enter n: "))

for i in range(1,n+1):
    for j in range(i-1):
        print(" ",end="")
    for k in range(n):
        print("*",end="")
    n-=1
    print()



n=int(input("Enter n: "))
s=1
for i in range(n,0,-1):
    for j in range(i-1):
        print(" ",end="")
    for k in range(s):
        print("* ",end="")
    s+=1
    print()
d=1
for j in range(n,1,-1):
    for k in range(d):
        print(" ",end="")
    d+=1
    for t in range(j-1):
        print("* ",end="")
    print()



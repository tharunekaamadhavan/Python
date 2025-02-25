n=int(input("Enter n: "))
s=1
for i in range(n,0,-1):
    for j in range(i-1):
        print(" ",end="")
    for k in range(s):
        print("* ",end="")
    s+=1
    print()
u=1
for r in range(n,1,-1):
    for t in range(u):
        print(" ",end="")
    u+=1
    for v in range(r-1):
        print("* ",end="")
    print()

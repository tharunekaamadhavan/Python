n=5
a=n-1
s=0
for i in range(n,0,-1):
    for j in range(i):
        for k in range(s):
            if s<a:
                print(" ",end="")
        print("*")
        s=s+1
    print()
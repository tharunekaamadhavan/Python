n=int(input("Enter n: "))
for i in range(n):
    for j in range(0,i+1):
        print(end=" ")
    for j in range(0,n-i):
        print("*",end=" ")
    print()

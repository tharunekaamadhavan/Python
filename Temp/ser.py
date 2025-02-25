n=int(input("Enter n: "))
for i in range(n):
    for j in range(n-i):
        print(i+1,end=" ")
    for j in range(j+1):
        print(end=" ")
    print()

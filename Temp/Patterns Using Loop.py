a="*"
n=int(input("Enter the number of lines: "))
for i in range(n,0,-1):
    print(a*i)


a="*"
n=int(input("Enter the number of lines: "))
s=0
for i in range(n,0,-1):
    print(" "*s,end="")
    print(a*i)
    s+=1



n=int(input("Enter the number of line: "))
s=n-1
for i in range(1,n+1):
    print(" "*s,end="")
    print("*"*i)
    s-=1

   
n=int(input("Enter the number of rows: "))
s=n-1
for i in range(1,n+1):
    print(" "*s,end="")
    print("* "*i)
    s-=1

n=int(input("Enter the number of rows: "))
s=n-1
for i in range(1,n+1):
    print(" "*s,end="")
    print("* "*i)
    s-=1
s=1
for i in range(n-1,0,-1):
    print(" "*s,end="")
    print("* "*i)
    s+=1


n=int(input("Enter n: "))
for i in range(n,0,-1):
    print("*"*i)
for i in range(2,n+1):
    print("*"*i)
    

n=int(input("Enter n: "))
for i in range(1,n+1):
    print("*"*i)
for i in range(n-1,0,-1):
    print("*"*i)




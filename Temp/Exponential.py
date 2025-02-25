def exp(x,y):
    if y==0:
        return 1
    else:
        return x*exp(x,y-1)
x=int(input("Enter x: "))
y=int(input("Enter y: "))
print("Exponentiation: ",exp(x,y))

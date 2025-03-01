print("Swapping without variables")
a=int(input("Enter a: "))
b=int(input("Enter b: "))
print("Before swapping: ")
print("a= ",a)
print("b= ",b)
a=a+b
b=a-b
a=a-b
print("After swapping: ")
print("a= ",a)
print("b= ",b)
print("Swapping with variables")
a=int(input("Enter a: "))
b=int(input("Enter b: "))
print("Before swapping: ")
print("a= ",a)
print("b= ",b)
c=0
c=a
a=b
b=c
print("After swapping: ")
print("a= ",a)
print("b= ",b)

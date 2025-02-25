a=int(input("a: "))
b=int(input("b: "))
if(a>b):
    a,b=b,a
rem=a%b
while rem!=0:
    a=b
    b=rem
    rem=a%b
print("gcg: ",b)

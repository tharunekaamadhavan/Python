b=int(input("base: "))
e=int(input("exponentiation: "))
res=b
while e>1:
    res=res*b
    e=e-1
print(res)

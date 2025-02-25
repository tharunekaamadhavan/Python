a=0
b=1
n=eval(input("Enter the number of terms: "))
print("Fibonacci Series: ")
print(a)
print(b)
for i in range(n):
 c=a+b
 print(c)
 a=b
 b=c

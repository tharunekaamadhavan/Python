n=int(input("enter n: "))
def newton(n):
    root=n/2
    for i in range(10):
        root=(root+n/root)/2
    print(root)
newton(n)

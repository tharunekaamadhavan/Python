class gcd:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def GCD(self):
        if self.a>self.b:
            self.a,self.b=self.b,self.a
        n=1
        gcd=0
        while n<=self.a:
            if self.a%n==0 and self.b%n==0:
                gcd=n
            n+=1
        print("GCD:",gcd)
a=int(input("Enter a:"))
b=int(input("Enter b:"))
g=gcd(a,b)
g.GCD()

class fibo:
    def __init__(self,num):
        self.num=num
    def fibona(self):
        n1,n2=0,1
        count=0
        if num<0:
            print("Enter positive number")
        elif num==1:
            print("Fibonacci of 1:",n2)
        else:
            while count<num:
                print(n1)
                nth=n1+n2
                n1=n2
                n2=nth
                count+=1
num=int(input("Enter num:"))
fi=fibo(num)
fi.fibona()
            
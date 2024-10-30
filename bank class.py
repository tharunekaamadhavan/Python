class bank:
    def __init__(self):
        self.balance=0
        print("Welcome to bank!!")
    def deposit(self):
        inpu=float(input("Enter the amount to be deposited:"))
        self.balance+=inpu
        print("Amount deposited:",inpu)
    def withdraw(self):
        inpu=float(input("Amount to be withdrawn:"))
        if inpu>self.balance:
            print("Insufficient balance")
        else:
            self.balance-=inpu
            print("Amount Withdrawn:",inpu)
    def fin(self):
        print("Amount in bank:",self.balance)
a=bank()
a.deposit()
a.withdraw()
a.fin()
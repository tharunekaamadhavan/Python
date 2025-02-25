class leap:
    def inp(self):
        self.yr=int(input("Enter year: "))
class check(leap):
    def checking(self):
        if self.yr%4==0:
            print("Leap year")
        else:
            print("Not leap year")
s=check()
s.inp()
s.checking()

    



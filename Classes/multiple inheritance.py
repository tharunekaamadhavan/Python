class parent1():
    def company(self,name,loc):
        self.name=name
        self.loc=loc
        print("name com:",self.name)
        print("loc com:",self.loc)
class parent2():
    def emp(self,ename,skill):
        
        print("name emp:",ename)
        print("skill com:",skill)
class child(parent1,parent2):
    def use(self,pos,note):
        
        print("pos:",pos)
        print("note:",note)
a=child()
a.company("tesla","berlin")
a.emp("tharunekaa","ai creator")
a.use("ai scientist","Extreemly talented")

    
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def disp(self):
        print("person details fnc")
        print(self.name)
        print(self.age)
class Employee(Person):
    def __init__(self,name,age,id):
        super().__init__(name,age)
        self.empid=id
    def disp(self):
        print("in child class disp method")
        print(self.name)
        print(self.age)
        print(self.empid)
person=Person('Peter','21')
person.disp()
a=Employee('Peter',21,'uy7778')
a.disp()
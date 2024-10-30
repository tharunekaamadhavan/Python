from abc import ABC
class Animal(ABC):
    def move(self):
        pass
class Lion(Animal):
    def move(self):
        print("I roar")
class Dog(Animal):
    def move(self):
        print("I bark")
class Snake(Animal):
    def move(self):
        print("I crawl")
class Human(Animal):
    def move(self):
        print("I walk")

a=Lion()
a.move()
a=Dog()
a.move()
a=Snake()
a.move()
a=Human()
a.move()
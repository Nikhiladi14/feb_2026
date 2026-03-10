#polymorphism
class Dog:
    def sound(self):
        print("Dog barks")

class Cat:
    def sound(self):
        print("Cat meows")

animals = [Dog(), Cat()]

for animal in animals:
    animal.sound()


#Encapsulation 
#public 
class Student:
    def __init__(self, name):
        self.name = name  

    def display(self):     
        print("Name:", self.name)


s = Student("Nikhil")
print(s.name)     
s.display()        

#protected
class Student:
    def __init__(self, name):
        self._marks = 85   # Protected variable


class Result(Student):
    def show_marks(self):
        print("Marks:", self._marks)


r = Result("Nikhil")
r.show_marks()     
print(r._marks)   

#private

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.__marks = marks   # Private variable

    def get_marks(self):       # Public method to access private data
        return self.__marks


s = Student("Nikhil", 90)

print(s.name)      
print(s.get_marks())  

#Abstraction 

from abc import ABC, abstractmethod

class Animal(ABC):   # Abstract class

    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):
    def sound(self):
        print("Dog barks")


class Cat(Animal):
    def sound(self):
        print("Cat meows")


d = Dog()
c = Cat()

d.sound()
c.sound()
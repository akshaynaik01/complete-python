# Inheritance
  # Inheritance is the mechanism by which a class(child) can use the properties and methods of another class(parent).
  
class Animal:           # parent class,super class
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def info(self):
        print(f"Your name is {self.name} and Your age is {self.age}")
        
        
class Human(Animal):     #child class,sub class
    def __init__(self, name, age,number,group):
        super().__init__(name, age)
        self.number = number
        self.group = group

class Robots(Human):
    def __init__(self, name, age, number, group,imei):
        super().__init__(name, age, number, group)
        self.imei = imei

obj = Animal("lion",12)
obj2 = Human("akshay",20,121221122,"B+")

obj2.info() 



# Encapsulation
  # Encspsulation means bundling data(attributes) and methods into one units(class)


class Animal:
    name = "Lion"
    
    def speak(self):
        print("Hello I will roar")
        
obj = Animal()

print(obj.name)

obj.name = "ibra"
print(obj.name)



# Polymorphism
   # Polymorphism allows different classes to define methods with the same name but different behavious.


class Animal:
    name = "lion"
    def speak(self):
        print("Hello I roar")
        
class Bird:
    name = "sparrow"
    
    def speak(seelf):
        print("Hello I Tweet")
        
obj = Animal()
obj2 = Bird()

obj.speak()
obj2.speak()


class Animal:
    name = "lion"
    
    def speak(self):
        print("Hello i roar")
        
class Human(Animal):
    name = "Akshay"
    
    def speak(self):
        print("Hello my name is akshay")
        
    
obj = Human()
obj2.speak()



# Abstraction
   # Abstraction is used to simplifying complex systems by focusing on essential features and hiding unnecessary details.

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass
    
class Dog(Animal):
    def sound(self):
        print("Hello I make woof method")
    def hello(self):
        print("I am a dog and I woof")
        
class Cat(Animal):
    def sound(self):
        print("Hello I make meow sound")
        
        
obj = Dog()
obj2 = Cat()

obj.sound()
obj.hello()
obj2.sound()







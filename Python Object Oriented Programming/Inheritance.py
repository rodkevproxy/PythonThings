# Inheritance = Allows a class to inherit attributes and methods from another class 
#               Helps with code reusability and extensibility 
#               Class Child(Parent)
# This allows you to usew attributes and methods from another class 

class Animal: 
    def __init__(self, name): #This is how you define the contructor 
        self.is_alive = True
        self.name = name 

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")

class Dog(Animal):
     pass 

class Cat(Animal): 
    pass 

class Mouse(Animal): 
    pass 

dog = Dog("Dollar")
cat = Cat("Pepe")
mouse =Mouse("Jerry")




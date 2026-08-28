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
     def speak(sekf): 
         print("WOOF! ")

class Cat(Animal): 
    def speak(self):
        print("MEOW! ")

class Mouse(Animal): 
    def speak(self):
        print("SQUEEK! ")

dog = Dog("Dollar")
cat = Cat("Pepe")
mouse =Mouse("Jerry")

#Now to test that we can use attributes from another classes i am goin to write the following instructions 

print(dog.name) #This is an inheritance of an attribute from the class Animal
print(dog.is_alive)
cat.eat()
cat.sleep() #This is an inheritance of a method from the class Animal

dog.speak()
cat.speak()
mouse.speak()


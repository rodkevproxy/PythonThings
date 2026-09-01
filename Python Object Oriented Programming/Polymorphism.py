#Polymorphism = Greek word that means ti "have any forms or faces"
#                               poly = Many
#                               morphe = Form 
#                           
#                           TWO WAYS TO ACHIEVE POLYMORPHISM 
#                          1. Inheritance = An object could be treated the same type as a parent class 
#                          2. "Duck Typing" = Object must have necessary attribute/methods

#On this file we will be more focused on the first one 


from abc import ABC, abstractmethod
class Shape():
    @abstractmethod #This is called a decirator
    def area(self): #This is an abstract method 
        pass
        

class Circle(Shape): 
    def __init__(self, radious):
        self.radious = radious 

    def area(self):
        return 3.14 * self.radious ** 2 

class Square(Shape):
    def __init__(self, side):
        self.side = side 

    def area(self):
        return self.side ** 2 

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base 
        self.height = height

    def area(self): 
        return self.base * self.height * 0.5 
 
shapes = [Circle(4), Square(5), Triangle(7, 6)]

for shape in shapes: 
    print(shape.area())

    
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

class Square(Shape):
    def __init__(self, area):
        self.area = area 

class Triangle(Shape):
    def __init__(self, ):
        pass #Just for now 

square = Square() #So here our "square" identifies as a "Square" and science "Square" inheritates from "Shape" is also considered a "Shape", so those are two possible forms for square 

shapes = [Circle(), Square(), Triangle()]
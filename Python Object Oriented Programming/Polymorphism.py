#Polymorphism = Greek word that means ti "have any forms or faces"
#                               poly = Many
#                               morphe = Form 
#                           
#                           TWO WAYS TO ACHIEVE POLYMORPHISM 
#                          1. Inheritance = An object could be treated the same type as a parent class 
#                          2. "Duck Typing" = Object must have necessary attribute/methods

#On this file we will be more focused on the first one 

class Shape():
    pass 

class Circle(Shape): 
    pass 

class Square(Shape):
    pass 

class Triangle(Shape):
    pass

square = Square() #So here our "square" identifies as a "Square" and science "Square" inheritates from "Shape" is also considered a "Shape" 
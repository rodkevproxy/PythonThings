# super() = Function used in a child class to call methods from a parent class (superclass).
#           Allows you to extend the functionality of the inherited methods 

class Shape:  #This is the super class, dont forget to setup this class into the other classes so they can inherate the attributes
       def __init__(self, colour, is_filled): 
              self.colour = colour 
              self.is_filled = is_filled 

       def describe(self):
              print(f"It is {self.colour} and {"filles" if self.filled == True else "Not Filled"}")
              
              



class Circle(Shape):
     def __init__(self, colour, is_filled, radious):
           super().__init__(colour, is_filled)
           self.radious = radious 
          

class Square(Shape):
     def __init__(self, colour, is_filled, width):
               super().__init__(colour, is_filled)
               self.width = width 

class Triangle(Shape):
     def __init__(self, colour, is_filled, width, height):
               super().__init__(colour, is_filled)
               self.width = width 
               self.height = height 


#Here when creating the object we have two ways to do it, both do the same, but has more focus on readability by using keyword arguments 
circle = Circle("blue", True, 5) #No keyword arguments 

square = Square(colour="Blue", is_filled=False, width=90) #With keyword argumnets 
triangle = Triangle(colour="Red", is_filled=True, width=23, height=20) 


circle.describe()




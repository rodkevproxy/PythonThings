# @Property = Decorator to define a method as a property (it can be accessed like an attribute)
#               Benefit: Add additional logic when read, write, or delete attributes 
#               Gives you getter, setter and deleter methods 

class Rectangle:
    def __init__(self, width, height): 
        self.width = self.width
        self.height = height

    rectangle = Rectangle(3, 4)

    print(rectangle.width)
    print(rectangle.height)

    #
    
 
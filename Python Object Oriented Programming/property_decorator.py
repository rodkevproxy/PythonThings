# @Property = Decorator to define a method as a property (it can be accessed like an attribute)
#               Benefit: Add additional logic when read, write, or delete attributes 
#               Gives you getter, setter and deleter methods 

class Rectangle:
    def __init__(self, width, height): 
        self._width = self.width  #To make attributes private or meant to be protected, prefix the attributes with "_"
        self._height = height
    @property
    def width(self): 
        return f"{self._width:.1f}cm"

    @property
    def height(pass): 
        pass 



    rectangle = Rectangle(3, 4)

    print(rectangle.width)
    print(rectangle.height)

    

 
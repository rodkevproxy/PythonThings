# Static Methods = A method that belong to a class rather than any object from that class (instance) 
#                   Usually used for functions 

# Instance Methods = Best for operations on instances of the class (objects)
# Static Methods = Best for utility functions that do not need access to class data 
# i have to continiue with this today 

class Employee: 
    def __init__ (self, name, position):
        self.name = name 
        self.position = position 

    #Example of instance method
    def get_info(self):
        return f"{self.name} = {self.position}"
    


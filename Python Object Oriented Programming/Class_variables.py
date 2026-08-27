# Class variables = Shared among all instances of a class 
#                   Defined outside the constructor 
#                   Allow you to share data among all objetcs created from that class 

class Student: 
    def __init__(self, name, age): 
        self.name = name 
        self.age = age 
        
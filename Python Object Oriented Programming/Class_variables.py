# Class variables = Shared among all instances of a class 
#                   Defined outside the constructor 
#                   Allow you to share data among all objetcs created from that class 

class Student: 

    #Class variable. These are difined outside the constructor



    def __init__(self, name, age): 
        self.name = name #These are instance variables
        self.age = age 

student1 = Student("Spongebob", 30)
student2 = Student("Bob", 19)
print(student1.name)
print(student2.age)




# Class variables = Shared among all instances of a class 
#                   Defined outside the constructor 
#                   Allow you to share data among all objetcs created from that class 

class Student: 

    #Class variable. These are difined outside the constructor
    #You can access these classes wiht an object, also is a good practice to access the class by the name of the class Ex. "Student.class_year"
    class_year = 2024



    def __init__(self, name, age): 
        self.name = name #These are instance variables
        self.age = age 

student1 = Student("Spongebob", 30)
student2 = Student("Bob", 19)
print(student1.name)
print(student2.age)




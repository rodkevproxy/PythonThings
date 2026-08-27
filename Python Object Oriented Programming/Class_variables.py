# Class variables = Shared among all instances of a class 
#                   Defined outside the constructor 
#                   Allow you to share data among all objetcs created from that class 

class Student: 

    #Class variable. These are difined outside the constructor
    #You can access these classes wiht an object, also is a good practice to access the class by the name of the class Ex. "Student.class_year"
    class_year = 2024
    num_students = 0 



    def __init__(self, name, age): 
        self.name = name #These are instance variables
        self.age = age 
        Student.num_students += 1 #Here because we are modifing a class variable, we will not use "self", instead we use the name of the class, in this case Student 

student1 = Student("Spongebob", 30)
student2 = Student("Bob", 19)
#To make sure that the counter is working, i will add a third student 
student3 = Student("Kev", 21)
student4 = Student("Sandy", 27)

print(Student.num_students)






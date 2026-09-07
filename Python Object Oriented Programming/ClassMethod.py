#Class Methods = Allow operations related to the class itself 
                #Take (cls) as the first parameter, which represents the class itself

class Student: 
    count = 0

    def __init__(self, name, gpa):
        self.name = name 
        self.gpa = gpa 
        Student.count += 1

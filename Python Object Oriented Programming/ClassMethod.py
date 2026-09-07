#Class Methods = Allow operations related to the class itself 
                #Take (cls) as the first parameter, which represents the class itself

class Student: 
    count = 0

    def __init__(self, name, gpa):
        self.name = name 
        self.gpa = gpa 
        Student.count += 1

#INSTANCE METHOD 
    def get_info(self): 
        return f"{self.name}{self.gpa}"

    @classmethod
    def get_count(cls): 
        return f"The total count is {cls.count}"

student1 = Student("Me", 4)
student2 = Student("Not Me", 3)

print(Student.get_count())

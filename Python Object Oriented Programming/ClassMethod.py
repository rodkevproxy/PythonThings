#Class Methods = Allow operations related to the class itself 
                #Take (cls) as the first parameter, which represents the class itself
#Instance Methods: Best for operations on instances if the class (object)
# Static Methods: Best for utikity functions that do not need access to class data 
#Class Methods: Best for class-level data or require access to the class itself


class Student: #

    count = 0#
    total_gpa = 0 

    def __init__(self, name, gpa):
        self.name = name 
        self.gpa = gpa 
        Student.count += 1
        Student.total_gpa += gpa 

#INSTANCE METHOD 
    def get_info(self): 
        return f"{self.name}{self.gpa}"

    @classmethod
    def get_count(cls): 
        return f"The total count is {cls.count}"


    @classmethod
    def avrg_gpa(cls): 
        if cls.count == 0: 
            return 0 
        else: 
            return f"Average GPA{cls.total_gpa / cls.count:.2f}"

student1 = Student("Me", 4)
student2 = Student("Not Me", 3)

print(Student.get_count())
print(Student.avrg_gpa())


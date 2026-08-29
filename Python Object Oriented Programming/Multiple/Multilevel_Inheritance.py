# multiple inheritance = inherit from more than one parent class 
#                         C(A,B)


# multilevel inheritance = inherit from a pareent which inherits from another parent 
#                           C(B) <- B(A) <- A 


class Prey: #Parent class
    def flee(self):
        print("You can now flee i guess..? ")

class Predator: #Parent class
    pass 

class Rabbit: #Child class
    pass 

class Hawk: #Child class
    pass 

class Fish: #Child class
    pass 


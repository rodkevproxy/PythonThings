# multiple inheritance = inherit from more than one parent class 
#                         C(A,B)


# multilevel inheritance = inherit from a pareent which inherits from another parent 
#                           C(B) <- B(A) <- A 


class Prey: #Parent class
    def flee(self):
        print("This animal is fleeing")

class Predator: #Parent class
    def hunt(self):
        print("This animal is hunting ")

class Rabbit(Prey): #Child class
     

class Hawk(Predator): #Child class
    pass 

class Fish(Predator, Prey): #Child class
    pass 




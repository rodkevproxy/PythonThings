# multiple inheritance = inherit from more than one parent class 
#                         C(A,B)


# multilevel inheritance = inherit from a pareent which inherits from another parent 
#                           C(B) <- B(A) <- A 

class Animal():
    def __init__(self,name): #This is how you define a constructor 
        self.name = name

    def eat(self):
        print("This animal is eating ")

    def skeep(self): 
        print("This animal is sleeping ")
class Prey(Animal): #Parent class
    def flee(self):
        print("This animal is fleeing")

class Predator(Animal): #Parent class
    def hunt(self):
        print("This animal is hunting ")

class Rabbit(Prey):
    pass #Child class
     

class Hawk(Predator): #Child class
    pass 

class Fish(Predator, Prey): #Here this is an example of multiple inheritance 
    pass 


#Here i created the objests 

rabbit = Rabbit()
hawk = Hawk()
fish = Fish()

fish.flee()

rabbit.eat()
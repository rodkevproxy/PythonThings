# multiple inheritance = inherit from more than one parent class 
#                         C(A,B)


# multilevel inheritance = inherit from a pareent which inherits from another parent 
#                           C(B) <- B(A) <- A 

class Animal():
    def __init__(self, name): #This is how you define a constructor 
        self.name = name

    def eat(self):
        print(f"{self.name} is eating ")

    def skeep(self): 
        print(f"{self.name} is sleeping ")
class Prey(Animal): #Parent class
    def flee(self):
        print(f"{self.name} is fleeing")

class Predator(Animal): #Parent class
    def hunt(self):
        print(f"{self.name} is hunting ")

class Rabbit(Prey):
    pass #Child class
     

class Hawk(Predator): #Child class
    pass 

class Fish(Predator, Prey): #Here this is an example of multiple inheritance 
    pass 


#Here i created the objests 

rabbit = Rabbit("Toby")
hawk = Hawk("Tony")
fish = Fish("Dory")

fish.flee()

rabbit.eat()
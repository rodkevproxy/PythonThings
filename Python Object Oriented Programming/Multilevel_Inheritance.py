# multiple inheritance = inherit from more than one parent class 
#                         C(A,B)


# multilevel inheritance = inherit from a pareent which inherits from another parent 
#                           C(B) <- B(A) <- A 

class Animal():
    def __init__(self, name, lastname): #This is how you define a constructor 
        self.name = name
        self.lastname = lastname
    def eat(self):
        print(f"{self.name} is eating ")

    def sleep(self): 
        print(f"{self.name} {self.lastname} is sleeping ")
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

rabbit = Rabbit("Toby", "Rodas")
hawk = Hawk("Tony", "Rodas")
fish = Fish("Dory", "Rodas")

rabbit.sleep()


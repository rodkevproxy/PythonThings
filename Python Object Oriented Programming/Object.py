# object = A "bundle" of related attributes (Variables) and methods (functions) 
# Ex. phone, cup, book
# You need a class to create many objects 

# Class = (blueprint) used to desing the structure and layout of an object 

class Car: 
    def __init__(self, model, year, colour, for_sale): #This is the constructor method, this is required in order to construct objects 
        self.model = model 
        self.year = year
        self.colour = colour 
        self.for_sale = for_sale 

car1 = Car("Mustang", 2024, "Red", False)


#print(car1) If we atempt this, what wi will end up getting is the memory address location of where the object is

print(car1.model, car1.year) # This dot is known as the attribute access operator 

#Clases can be re used, here is a quick example by creating a secong car with different specs 

car2 = Car("GT3", 2027, "Black", True)

print(car2.model, car1.model)
print(car1.for_sale)




# object = A "bundle" of related attributes (Variables) and methods (functions) 
# Ex. phone, cup, book
# You need a class to create many objects 

# Class = (blueprint) used to desing the structure and layout of an object 

#Clases can be re used, here is a quick example by creating a secong car with different specs 
#print(car1) If we atempt this, what wi will end up getting is the memory address location of where the object is


from carClass import Car 

car1 = Car("Mustang", 2024, "Red", False)
car2 = Car("GT3", 2027, "Black", True)



car1.drive()
car2.stop()
car2.describe()







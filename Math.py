import math # This imports the math module for python 

# Here im seeing the math and related things that i will need later 

# friends = friends + 1 
# Shorter way to write this line of code 
# friends += 1 # This line of code does the same job but shorter 

# **= this is means "to the power"
# % this is modulus, which is basically the remainder of any division 


#Built in math functions 

# round, as its name tell us it rounds numbers e.g round(value, number of decimal digits)
# abs, this one tell us the absolute value, which is the value of a number away from zero 
# this will give us the value of a number to the power of another numeber e.g resul = (pow 4, 5) 


# print (math.pi) this print the value of pi 
# print (math.e) this print the exponensial constant 

# result = math.sqrt(x) this is the square root 
# result = math.ceil(x) This will round a number up 
# result = math.floor(x) This will round a number down 

# Practice 

radius = float(input("Enter the radius of a circle: "))

circunference = 2 * math.pi * radius

print (f"The circunference is {round(circunference, 2)}cm")


#Area of a circle 

area = math.pi * pow(radius, 2)

print (f"The area is {round(area, 2)}")


a = float(input("Enter side A "))
b = float(input("Enter side B"))

c = math.sqrt(pow(a, 2) + pow(b, 2))


print (f"Side C is {c}")





















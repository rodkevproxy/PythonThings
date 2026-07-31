# How to generate random numbers in python

import random 

# Fuction that generates a random interger 

number = random.randint(1, 6)
print (number)

low = 6 
high = 60 
options = ("rock", "paper", "scissors")

number = random.randint(low, high)

number = random.random() #This will return a point decimal number 

option = random.choice(options)


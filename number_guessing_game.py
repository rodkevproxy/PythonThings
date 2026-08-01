# Number guessing game to practice with the random module 

import random 

lowest_value = 1 
highest_value = 100 
answer = random.randint(lowest_value, highest_value)
guesses = 0 
is_running = True 

print("Python Number Guessing Game")

print(f"Select a number betweer {lowest_value} and {highest_value}")



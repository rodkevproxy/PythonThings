# Number guessing game to practice with the random module 

import random 

lowest_value = 1 
highest_value = 100 
answer = random.randint(lowest_value, highest_value)
guesses = 0 
is_running = True 

print("Python Number Guessing Game")

print(f"Select a number betweer {lowest_value} and {highest_value}")


while is_running: 

    guess = input("Enter your guess: ")

    if guess.isdigit():
        guess = int(guess)
        guesses += 1 

        if guess < lowest_value or guess > highest_value:
             print("That guess is out of range")
             print(f"Select a number betweer {lowest_value} and {highest_value}")
       
    else: 
        print("invalid digit")
        print(f"Select a number betweer {lowest_value} and {highest_value}")



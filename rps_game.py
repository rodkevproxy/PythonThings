# Rock Paper Scissors game 
# i will try my self first taking in consideration the things learned before 
import random

options = ("Rock",
           "Paper", 
           "Scissors")

player = None
answer = random.choice(options)
 

while player not in options:
    player = input("Enter a choice (Rock, Paper and Scissors)")

print(f"Player choice was: {player}")
print(f"Computer choice was: {answer}")

# Win conditions 
if player == answer: 
    print("It is a tie")
if player == "Rock" and answer == "Scissors":
    print("You win")
if player == "Paper" and answer == "Rock": 
    print("You win")
if player == "Scissors" and answer == "Paper":
    print ("You win")

# Loose conditions 

if answer == "Paper" and player == "Rock":
    print("You loose")
if answer == "Rock" and player == "Scissors":
    print("You loose")
if answer == "Scissors" and player == "Paper":
    print("You loose")

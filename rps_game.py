# Rock Paper Scissors game 
# i will try my self first taking in consideration the things learned before 
import random

options = ("Rock",
           "Paper", 
           "Scissors")
game_running = True 



while game_running:
    player = None
    answer = random.choice(options)

    while player not in options:
        player = input("Enter a choice (Rock, Paper and Scissors)")

    print(f"Player choice was: {player}")
    print(f"Computer choice was: {answer}")

    # Win conditions 

    if player == answer: 
        print("It is a tie")
    elif player == "Rock" and answer == "Scissors":
        print("You win")
    elif player == "Paper" and answer == "Rock": 
        print("You win")
    elif player == "Scissors" and answer == "Paper":
        print ("You win")

    # Loose conditions 

    else: 
        print("You loose")

    # Temporary variable to end the game 

    play_again = input("Would you like to play again> (Y/N)").lower()
    if not play_again == "y":
        game_running = False

print("Thanks for playing!")




        

 


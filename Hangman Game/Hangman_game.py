import random
import time

words = ("Apple", "Banana", "Coconut", "Kiwi", "Mango", "Strawberry", "Cherry")

#Now the functions and extra things that we will need for this game

#Once we reac 6 incorrected guesses we loose the game 
#Dicionary of key():
#ASCII art
hangman_art = {0:("     ",
                  "     ",
                  "     "), 
               1:("  o  ",
                  "     ",
                  "     "), 
               2:("  o  ",
                  "  |  ",
                  "     "), 
               3:("  o  ",
                  "  |\\",  #The back slash is a escape sequence on a string, se i use two of them to display one
                  "     "), 
               4:("  o  ",
                  " /|\\",
                  "     "), 
               5:("  o  ",
                  " /|\\",
                  " /   "), 
               6:("  o  ",
                  " /|\\",
                  " / \\")}


def display_man (wrong_guesses): 
    print("***************")
    for line in hangman_art[wrong_guesses]:
        print(line)
    print("***************")


def display_hint (hint):
    print(" ".join(hint))
    


def display_answer(answer): 
     print(" ".join(answer))

def main():
    answer = random.choice(words)
    hint = ["_"] * len(answer)
    wrong_guesses = 0 
    guessed_letters = set()  #To create an empty set it has to be done in this way     
    is_running = True

    while is_running:
        display_man(wrong_guesses)
        display_hint(hint)
        guess = input("Enter a letter: ").lower()#

        #Input validation 
        if len(guess) != 1 or not guess.isalpha(): 
            print("Invalid Inpuit")
            continue

        if guess in guessed_letters: 
            print(f"{guess} is already guessed")
            continue

        guessed_letters.add(guess)



        #Now here i added the for loop that will find if there is a match and replace it 
        if guess in answer: 
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess 
        else:
         wrong_guesses += 1 

         if "_" not in hint: 
             is_running = False
             print("Congrats")
             display_man(wrong_guesses)
             display_answer(answer)
         elif wrong_guesses >= len(hangman_art) - 1: 
             is_running = False
             print("You Lost")
             display_man(wrong_guesses)
             time.sleep(2)
             print("The correct answer was...")
             time.sleep(2)
             display_answer(answer)
             
               
if __name__ == '__main__':
    main()










    






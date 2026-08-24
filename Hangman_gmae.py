import random

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
    pass 

def display_hint (hint):
    pass

def display_answer(answer): 
    pass

def main():
    pass


if __name__ == '__main__':
    main()

#Frame x race is using fedex 







    






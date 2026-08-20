# Beginners guide to create a slot machine 

import random

def spin_row(): 
    symbols = ["🍒", "⭐", "🔔", "🃏"]

def print_row(): 
    pass

def pay_out():
    pass 

def main():
    balance: 100 
    print("**************************")
    print("Welcome to Python Slots ")
    print("Symbols: 🍒, ⭐, 🔔, 🃏")
    print("**************************")


    while balance > 0: 
        print(f"Current balance £{balance}")

        bet = int(input("Place your bet amount: "))

        if not bet.isdigit():   #Useful line of code when we want to check if am imput is a digit
            print("That is not a valid input")
            continue

        if bet > balance: 
            print("Insuficient founds")
            continue

        if bet <= 0: 
            print("Bet must be greater than 0")
            continue

        balance -= bet

        row = spin_row() #This spin function is a list 



        

if __name__ == '__main__':
    main()





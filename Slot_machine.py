# Beginners guide to create a slot machine 

import random
import time

def spin_row(): 
    symbols = ["🍒", "⭐", "🔔", "🃏"]

    return [random.choice(symbols) for _ in range(3)] #This is the way to do a list coprenhension inside a function
                                                           #Here we do not create an extra list to store the values, we return the values directly, what most people do is to use a "_" as a place holder 
    
def print_row(row): 
    print(" | ".join(row)) #Built in method 

def pay_out(row, bet):
    if row [0] == row [1] == row[2]:
        if row[0] == "🍒":
            return bet * 2 
        elif row[0] == "⭐":
            return bet * 2.5
        elif row[0] == "🔔":
            return bet * 3
        elif row [0] == "🃏":
            return bet * 3
    return 0




     

def main():
    balance = 100 
    print("**************************")
    print("Welcome to Python Slots ")
    print("Symbols: 🍒, ⭐, 🔔, 🃏")
    print("**************************")


    while balance > 0: 
        print(f"Current balance £{balance}")

        bet = input("Place your bet amount: ")

        if not bet.isdigit():   #Useful line of code when we want to check if am imput is a digit
            print("That is not a valid input")
            continue

        bet = int(bet) #Here bet has to be typecasted apart due to the isdigit fucntion, and has to be palced after the isdigit check 

        if bet > balance: 
            print("Insuficient founds")
            continue

        if bet <= 0: 
            print("Bet must be greater than 0")
            continue

        balance -= bet

        row = spin_row() #This spin function is a list 
        print("Spinning...")

        time.sleep(1)

        print_row(row)

        payout = pay_out(row, bet)

        if payout > 0: 
            print(f"Congrats you won £{payout} ")
        else:
            print("Sorry you lost this round")

        balance += payout

        play_again = input("Do you want to play again? (Y/N) ").upper()

        if play_again != "Y":
            break





        

if __name__ == '__main__':
    main()





# Beginners guide to create a slot machine 

import random

def spin_row(): 
    symbols = ["🍒", "⭐", "🔔", "🃏"]

    return [random.choice(symbols) for _ in range(3)] #This is the way to do a list coprenhension inside a function
                                                           #Here we do not create an extra list to store the values, we return the values directly, what most people do is to use a "_" as a place holder 
    







def print_row(): 
    pass

def pay_out():
    pass 

def main():
    balance = 100 
    print("**************************")
    print("Welcome to Python Slots ")
    print("Symbols: 🍒, ⭐, 🔔, 🃏")
    print("**************************")


    while balance > 0: 
        print(f"Current balance £{balance}")

        bet = (input("Place your bet amount: "))
        bet = int(bet) #Here bet has to be typecasted apart due to the isdigit fucntion

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





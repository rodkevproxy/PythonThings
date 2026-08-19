#Python Banking Program

def show_balance(balance):
    print(f"Your balance is {balance:.2f}")

def deposit():
    amount = float(input("Enter the amount to be deposited: "))
    if amount < 0: 
        return 0 
        print("That is not a valid amount")
    else: 
        return amount

def withdraw(balance):
    amount = float(input("Enter amount to be withdrawn: "))
    if amount > balance: 
        print("Insufficient founds")
        return 0
    elif amount < 0: 
        print("Amount should be greater than 0")
        return 0
    else: 
        return amount
    
def main ():
    balance = 0 
    is_running = True 

    while is_running: 
        print("Banking program")
        print("1.Show Balance")
        print("2.Deposit")
        print("3.Withdraw")
        print("4.Exit")

        choice = input("Please select an option (1-4): ")

        if choice == "1":
            show_balance(balance) #Because now we have put our code inside the main function, we have to pass the variables of balance to the other functions, and set up the parameters in the function
        elif choice == "2":
            balance += deposit()
        elif choice == "3":
            balance -= withdraw(balance)
        elif choice == "4":
            is_running = False 

        else: 
            print("That is not a valid option")

    print("Thank you, have a nice day")


if __name__ == '__main__':  #Including this line of code is a good practice, so the program can be imported 
    main()








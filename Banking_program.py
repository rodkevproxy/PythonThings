def show_balance():
    print(f"Your balance is {balance:.2f}")

def deposit():
    amount = float(input("Enter the amount to be deposited: "))
    if amount < 0: 
        return 0 
        print("That is not a valid amount")
    else: 
        return amount

def withdraw():
    amount = input("Enter amount to be withdrawn: ")

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
        show_balance()
    elif choice == "2":
        balance += deposit()
    elif choice == "3":
        withdraw()
    elif choice == "4":
        is_running = False 

    else: 
        print("That is not a valid option")


    







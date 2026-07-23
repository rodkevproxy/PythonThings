# Nested loop is a loop inside another loop 

# Here a small example where we print a rectangle using user input 

row = int(input("Enter the amount of rows "))
columns = int(input("Enter how many columns "))
symbol = input("Enter the sign that you want to use ") 

for x in range(row):
    for x in range(columns):
        print(symbol, end="")
    print()
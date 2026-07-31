# Creating a concession stand using dictionaries 

# First we create a menu using a dictionary

menu = {"pizza": 6.00,
        "burger": 10.0,
        "hot-Dog": 4.99,
        "ice cream": 4.99,
        "salad": 6.99}

cart = []
total = 0

for key, value in menu.items():
    print(f"{key:10}: ${value:.2f}")

print("-----------------------------------")

while True: 
    food = input("Select a food (q to quit): ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None: 
        cart.append(food)


print("----- YOUR ORDER -----")

for food in cart: 
    total += menu.get(food)
    print (food, end=" ")

print()
print(f"Your total is: {total:.2f}")


# Here i am using the method get with the dictionary 


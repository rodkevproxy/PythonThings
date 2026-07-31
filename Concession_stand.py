# Creating a concession stand using dictionaries 

# First we create a menu using a dictionary

menu = {"Pizza": 6.00,
        "Burger": 10.0,
        "Hot-Dog": 4.99,
        "Ice cream": 4.99,
        "Salad": 6.99}

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

print(cart)


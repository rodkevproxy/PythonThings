# WHile loop = execute some code WHILE some conditions remains true 

name = input("Enter your name: ")

while name == "":
    print("You did not enter your name")
    name = input("Enter your name: ")
print (f"Hello {name}")

age = int(input("Enter your age: "))

while age < 0:
    print("Your age cannot be negative")
    age = int(input("Enter your age: "))

print(f"Your age is {age}")

food = input("Enter your favourite food: (q to quit)")

while not food == "q":
    print(f"You like {food}")
    food = input("Enter antoher one: (q to quit)")

print ("C ya")

# This example uses the or logical operator 

num = int(input("Enter a number between 1 - 10: "))

while num < 0 or num > 10:
    print(f"{num} is not valid")
    num = int(input("Enter a number: "))

print(f"Your number was {num}")



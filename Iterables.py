#Iterables = An object/collection that can return its element one at a time, 
#            allowing it to be iterated over in a loop


numbers = [1, 2, 3, 4, 5]

for num in reversed(numbers): 
    print(num, end="-")

print()

fruits_tupple = ("Mango", "Fresa", "Banana", "Cocos", "Guanabana")

for fruit in fruits_tupple:
    print(fruit, end=" ")

print()

fruits = "Mango"

for letter in fruits:
    print(letter, end=" ")

print()

My_Dictionary = { "A" : 1, "B" : 2, "C" : 3, "D" : 4}


for key, value in My_Dictionary.items():
    print(f"{key} : {value}")

print("Iterables are done")












from script1 import *

def fav_drink(drink):
    print(f"Your favourite drink is {drink}")


def main():
    print("This is script 2")
    fav_food("Sushi")
    fav_drink("Coffee")
    print("Good bye")


if __name__ == '__main__':
    main()

print("This script is done")




# from script2 import * # Here __name__ is equals to string script2 


#print(__name__) #But here __name__ is equals to __main__, meaning we are running script1 directly 

def fav_food(food):
    print(f"Your favourite food is {food}")

def main():
    print("This is script 1")
    fav_food("Pizza")
    print("Good bye")
    
if __name__ == '__main__':
    main()







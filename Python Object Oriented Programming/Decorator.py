#Decotator = A function that extends the behaviour of another function 
#           w/o mofifying the base function 
#           pass the base fucntion as an argument to the decorator 

#Here is how to create a decorator 
def add_topping(func): 
    def wrapper():
        print("You added sprinkles")
        func()
    return wrapper 


@add_topping
def get_ice_cream(): 
    print("Here is your ice cream")

get_ice_cream()





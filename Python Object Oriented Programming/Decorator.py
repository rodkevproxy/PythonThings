#Decotator = A function that extends the behaviour of another function 
#           w/o mofifying the base function 
#           pass the base fucntion as an argument to the decorator 

#Here is how to create a decorator 
def add_sprinkles (func): 
    def wrapper(args, **kwargs): 
        print("You add sprinkles")
        func(*args, **kwargs)
    return wrapper

#Here we add a wrapper function so we dont call the function when we apply the decorator 
def add_fudge(func): 
    def wrapper(*args, **kwargs): 
        print("You add fudge")
        func(*args, **kwargs)
    return wrapper()
#Main function of a decorator is to extend a function 




@add_fudge
@add_sprinkles
def get_ice_cream(flavour):
    print(f"Here is your {flavour} ice cream")

get_ice_cream("Vanilla")





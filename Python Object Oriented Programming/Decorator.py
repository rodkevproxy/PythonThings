#Decotator = A function that extends the behaviour of another function 
#           w/o mofifying the base function 
#           pass the base fucntion as an argument to the decorator 

#Here is how to create a decorator 
def add_sprinkles (func): 
    def wrapper(): 
        print("You add sprinkles")
        func()
    return wrapper

#Here we add a wrapper function so we dont call the function when we apply the decorator 
def add_fudge(func): 
    def wrapper(): 
        print("You add fudge")
        func()
    return wrapper()





@add_fudge
@add_sprinkles
def get_ice_cream():
    print("Here is your ice cream")

get_ice_cream()





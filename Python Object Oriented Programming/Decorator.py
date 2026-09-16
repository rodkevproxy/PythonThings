#Decotator = A function that extends the behaviour of another function 
#           w/o mofifying the base function 
#           pass the base fucntion as an argument to the decorator 

#Here is how to create a decorator 
def add_topping(func): 
    def wrapper():
        print("You added sprinkles")
        func()
    return wrapper 


def add_fudge(func): 
    def wrapper(): 
        print("You added fudge")
        func()
    return wrapper


@add_fudge
@add_topping
def get_ice_cream(): 
    print("Here is your ice cream")

get_ice_cream()





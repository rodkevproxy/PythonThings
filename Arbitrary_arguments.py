# Args = allows you to pass multiple non-key arguments 
# **kwargs = allow you to pass multiple keyword0arguments 
#   * unpacking operator 
# 1.Positional 2. Default 3. Keyword 4. ARBITRARY 

# When replaciong the parameters with *args we are creating a tuple that we can work with, this is known as the unpacking operator 

def add (*args):   #This tuple also has built in methods or we can iterate over it using a loop, we can also change *args for *nums meaning numbers
    total = 0 
    for arg in args:
        total += arg
    return total 

print(add(1, 2, 4))

    

def display_name (*args):
    for arg in args:
        print(arg, end=" ")

display_name("Kevin", "Rodas")


# **kwargs, this creates a class of a dictionary 

def print_address (**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


print_address(Street="Coleridge Road",
              Borough="Islington", 
              Number="11",
              Postcode= "N43NY",
              Flat="B1")

# Excercise about creating a shippiing lable 

def shipping_lable(**kwargs):
    pass 


shipping_lable(Postcode="N43NY", 
               Street="Coleridge Road", 
               House_Number="11",
               Instructions="Leave at the outdoor", 
               Flat="Basement 1",
               Company="DHL",
               Special_Serive="Yes")







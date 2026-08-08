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


print_address(Street="TBC",
              Borough="TBC", 
              Number="TBC",
              Postcode= "TBC",
              Flat="TBC")

# Excercise about creating a shippiing lable 

def shipping_lable(*args, **kwargs):    # Always make sure that the *args are positioned before the **kwargs
    for arg in args:
        print(f"{arg}", end=" ")

    print()

    # Printing the kwargs using fstrings and get method, get method must be used with single quotes 

    print(f"{kwargs.get('Postcode')}")
    print(f"{kwargs.get('Street')} {kwargs.get('House_Number')} {kwargs.get('Instructions')}")
    

shipping_lable("Mr", "Default Name",
               Section="RailNetwork",
               Area="Hammersmith London",
               Is_It_IT="No",
               Finance="No",
               Rail_Worker="Yes",
               Rail_Not_Worker="No",)

def shipping_lable_non_uk (*args, **kwargs):
    for arg in args:
        print(f"{arg}", end=" ")

    print()


    print(f"{kwargs.get('Section')} {kwargs.get('Area')}{kwargs.get('Is_It_IT')}")


shipping_lable_non_uk("Mr", "Default Name",
                         Section="Tbc",
                         Area="Tbc",
                         Is_It_IT="No",
                         Finance="No",
                         Rail_Worker="Yes",
                         Rail_Not_Worker="No",)


address_south_america("Co", "Default City",
                           City="Default",
                           Company="Default_Preseted by the client",
                           Status="To Be Confirmed",
                           Type="Depending on the sender letter",)

def address_south_america(*args, **kwargs):
    for arg in args: 
        print(f"{arg}", end=" ")
        print()

        print(f"{kwargs.get('Company')} : {kwargs.get('Status')} : {kwargs.get('City')} : {kwargs.get('Type')}")


friends_names_uk("Mr", "Miss", "And everyting else ",
                 FirstOne="Jossua",
                 SecondOne="Not Jossua",
                 ThirdOne="Jefrey",
                 FourthOne="Ali",
                 FifthOne="Does Not Exist Yet")

def friends_names_uk (*args, **kwarg):
    for arg in args:
        print(arg, end=" ")
        print()

        print(f"{kwarg.get('FirstOne')}")




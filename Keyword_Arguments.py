# Now we are into the keyword arguments 

# Keyword Arguments: An argument preceded by an identifier 
#                    Helps with readability 
#                    Order of the arguments does not matter in this case  
#                     1. positoinal, 2. Default 3. Keyword 4. Arbutrary

def hello(greeting, title, first, last):
    print(f"{greeting}{title}{first}{last}")

hello("hello ", "mr ", "kevin ", "rodas ") #This is a conventional way where if you change the position of the arguments, the position will also change in the output 


def hello_keyword(greeting, title, first, last):
    print(f"{greeting}{title}{first}{last}")

hello_keyword(title="mr ", first="kevin ", last="rodas ", greeting="hello ") #Here the output will remain the same, even when the order of the argumnets is different from the order of the function paramenters

#Function to get a phone number 

def get_phone(countrycode, areacode, first, last):
    return(f"{countrycode}-{areacode}-{first}-{last}") # An fstring can also be returned without having to put a print function 

phone_number = get_phone(countrycode=44, areacode=0, first=75761, last=91101)

print(phone_number)




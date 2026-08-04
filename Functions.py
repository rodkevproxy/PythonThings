# leanring functions 
# Function are jsut block of code that can be used for one of more cases, re-usable code

def happy_birthday(name, age):     #Here "Name acts as temporary place holder"
    print(f"Learning functions with {name} and he is {age} old")

  
# Sending data using the parentheses when calling a function is called arguments 
happy_birthday("Kev", 20)
happy_birthday("Rod", 20)
happy_birthday("Gut", 20)
happy_birthday("And", 45)

# In this case the function is giving 4 different outputs depending on the paramentes given at the very begining 
#Fucntion to display an invoice 

def invoice_funtion (name, total, item):
    print(f"This is the invoice, Name: {name}, The total is {total}, and the item was {item}")

invoice_funtion("Kevin", "3003", "HyperBoomm Speaker")




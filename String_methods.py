name = input("Enter your name")

# result = len(name) this counts the amount of chracters inside the string 

# result = name.find("o") this finds the position, when it finds something this returns -1 
# result = name.rfind ("q") thsi does the same as the one above but reversed 
# name = name.capitalize() this only applies for the first letter 
# name = name.upper() This capatilaze all the characters 
# name = name.lower() This return all the characters lower case 
# result = name.isdigit() This returns true or false (boolean), and checks if the string content is only digits 
# result = name.isalpha() This returns a boolean also, checks if the string content is only alphabetical characters 
# result = phone_ number.count("-") This counts the amount of a specific assigned character 
# result = phone_number.replace("-", " ") This method replaces characters in this case we replaced the "-" with a blank space 


#To check methods we can use print(help(str))

#Challenge, validate user input 
# Username is no more than 12 characteres 
# Username must not contain spaces 
# Username must not contain digits 

#Solution made by me 

username = (input("Enter your user name"))

if len(username) > 12: 
    print ("User name ca not be more than 12 characterers")

elif not username.find (" ") == -1:
    print("User name can not contain blank spaces")

elif not username.isalpha(): 
    print("User name can not contain digits")

else:
    print(f"Your new user name is {username}")






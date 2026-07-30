# A dictionary is a collection of {key: value} pairs 
# They are ordered and changeable, but do not allow duplicates

capitals = {"UK": "London",
            "USA": "Washington D.C.",
            "India": "New Delhi"}

# To see all the atributes and methos of the dictionary we can write the following lines print (dir(capitals)
# This one shows helpfull commands too print (help(capitals))

#To get one of the values from the dictionary: 
print(capitals.get("USA"))

#To check if the value exists in the dictionary, we can use an if statement 

if capitals.get == ("UK"):
    print("That capitlas exists")
else: 
    print("That capital does not exist")

# Using the update method we can add a new value key 

capitals.update({"Germany": "Berlin"})

#Using the pop methos will remove specific values 

capitals.pop("UK")

#Using the variant of the pop method "popitem" we can remove the latest value of the dictionary

capitals.popitem()

#Using the method clear will clear the dictionary

capitals.clear()

# Using the method keys will return only the keys of the dictionary, in this example i will put on a variable 
# Also, technically keys is an object meaning that it will re-assemble a list


keys = capitals.keys()

# Keys can be used in a for loop, meaning you can iterate over every key 

for key in capitals.keys(): 
    print(key)

# To get all the values in the dictionary we have the values method 

values = capitals.values()

#We can use this with a for loop as well

for value in capitals.values():
    print(value)

# The items method return a 2d tupple 

items = capitals.items()

for key, value in capitals.items():
    print(f"{key}:{value}")










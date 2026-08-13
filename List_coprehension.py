# List coprehension = Is a precise way to create lists in Python
#                       Compact and easier to read than traditional loops 
#                       [Expresion for value in iterable if condition]


#Traditional way 
doubles = []

for x in range(1, 11):
    doubles.append(x * 2)
print(doubles)

#Now using [Expresion for value in iterable if condition] (checking a condition is optional)

doubles_2 = [x *2 for x in range(1, 11)] #This will return the same 

print(doubles_2)


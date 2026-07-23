# for loop = execute a block of code a fixed number of times 
# You can iterate over a range, stings, sequence, etc.

# reversed function can be used to count backwards
# (1, 11, 2) First number is the starting point, second number is the finish point not inclusive, and third one works
# steps to count 

# You can iterate over a string too 

credit_card = "1234-1234-1233-1233"

for x in credit_card: 
    print(x)

# Printing X but skippoing the numebr 13, to skip over an iteration we can use the "continiue" keyword

for x in range(1, 21): 
    if x == 13: 
        continue
    else: 
        print(x)



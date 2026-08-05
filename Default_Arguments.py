# default arguments: A defaukt value for certain paramenters
#                    default i used whem that argument is omitted 
#                    make your functions more flexible and reduce the number of arguments 
#                     1. positoinal, 2. Default 3. Keyword 4. Arbutrary
# Starting the day with default arguments im python

# Here is an example of a function using porsitonal parameters 
# This is how a normal function works, by giving it the parameters 

import time


def net_price (list_price, discount, tax):
    return list_price * (1 - discount) * (1 + tax)

# This function does the exact same work as the previous one, but it has default paramenters 

def new_net_price(list_price, discount=0,tax=0.006): #This fucntion is more flexible, it will also accept a second porameters, the function will use whatever is passed in, and then the default fucntion
    return list_price * (1 - discount) * (1 + tax)


# Next example is by creating a timer using functions and a for loop 

def count (star, end):
    for x in range (star, end + 1): #Important to notice that on a for loop the second statement is exclusive, so i am adding 1 to it 
        print(x)
        time.sleep(1)
    print("Done!")

#In order to add default arguments we need to make sure that they are after the positional arguments

def count_2 (end, start=0):
    for x in range(start, end + 1):
        print(x)
        time.sleep(1)
    print("Done!")


count_2(30, 20)













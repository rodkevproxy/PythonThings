# default arguments: A defaukt value for certain paramenters
#                    default i used whem that argument is omitted 
#                    make your functions more flexible and reduce the number of arguments 
#                     1. positoinal, 2. Default 3. Keyword 4. Arbutrary
# Starting the day with default arguments im python

# Here is an example of a function using porsitonal parameters 
# This is how a normal function works, by giving it the parameters 

def net_price (list_price, discount, tax):
    return list_price * (1 - discount) * (1 + tax)

print(net_price(200, 0.5, 0.05))






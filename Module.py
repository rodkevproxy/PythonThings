# Moddule = a file containing code you want to include in your program 
#           use "import" to include a module (built in or my own one)
#           useful to break up a large program reusable separate files 


# We can give this modules names 

#import math as m # This way we can change the name of the module 

#print(m.pi)

#To import specific things, we can use the following lines 

from math import pi #This line will import only the pi function (using this can cause name conflicts)

print(pi) #This way we can use it with any added code 

#How to do it properly 

import math # e is an exponensial constant 

a, b, c, d = 1, 2, 3, 4

print(math.e ** a)


















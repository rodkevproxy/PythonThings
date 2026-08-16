# Viable scope = where a variable is visible and accesible 

#Scope resolution = (LEGB) Local -> Enclosed -> Global -> Built in




def func1(): 
    print(x)

def func2():
    print(x)

x = 10

#Example of a global function 





def func1(): 
    a = 1 # This varible is local to function 1 
    print(a)

    def func2():
            b = 2 
            print(b)

            func2()
            #Example of a enclosed fuction 



#Built in example 
# Here we have two versions of e, but following the LEGB order, e will be assigned to a global value
from math import e 
e = 10
def func3():
    print (e)





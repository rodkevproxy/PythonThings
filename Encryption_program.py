import random 
import string 

chars = " " + string.punctuation + string.digits + string.ascii_letters #Here instead of writing every single character manually, i decided to used specific  sections from the imports 
#Right now, chars is a long string, now i need to convert every single character into a single string, so i will typecast the entire String in to a list 

chars = list(chars) #Here all the characters are a single string, insteadd of a single big one
print(chars)
key = chars.copy()

print(key)




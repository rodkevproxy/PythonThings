import random 
import string 

chars = " " + string.punctuation + string.digits + string.ascii_letters #Here instead of writing every single character manually, i decided to used specific  sections from the imports 
#Right now, chars is a long string, now i need to convert every single character into a single string, so i will typecast the entire String in to a list 

chars = list(chars) #Here all the characters are a single string, insteadd of a single big one
key = chars.copy()

random.shuffle(key)


print(f"Chars: {chars}")
print()
print(f"Key: {key}")

#ENCRYPT
plain_text = input("Enter a message to encrypt ")
chiper_text = " " #This is the name of the encrypted message 

for letter in plain_text: 
    index = chars.index(letter)
    chiper_text += key[index]

print(f"Original message: {plain_text}")
print(f"Encrypted message: {chiper_text}")

#DECRYPTION


chiper_text = input("Enter a message to Decrypt ")
plain_text = " " #This is the name of the normal text

for letter in chiper_text: 
    index = key.index(letter)
    plain_text += chars[index]

print(f"Encrypted message: {chiper_text}")
print(f"Original message: {plain_text}")











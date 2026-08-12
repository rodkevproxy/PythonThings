# Membership operators = used to test wether a value or variable is found in a sequence 
#                           (string, list, tuple, set and dictionary)
#                           1. in 
#                           2. not in


word = "apple"

letter = input("Guess a letter in the secret word: ")

#This membership operator will test if a value is within a sequence 
if letter in word: 
    print(f"There is a {letter}")
else:
    print(f"{letter} was not found")



#This membership operator will test if a value is NOT within a sequence 

word_2 = "Kevin"

letter_2 = input("Enter another one")

if letter_2 not in word_2: 
    print(f"{letter_2} is not in the secret word")
else: 
    print(f"{letter_2} is in the word")


#Another example 

students = {"Jossuas",
            "Kevin",
            "Jordy"}

student = input("Enter the name of the student: ")


if student is not students: 
    print(f"{student} was not found in {students}")
else:
    print(f"{student} was found in {students}")


 
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

letter_2 = input("Enter another one: ")

if letter_2 not in word_2: 
    print(f"{letter_2} is not in the secret word")
else: 
    print(f"{letter_2} is in the word")


#Another example 

students = {"Jossua",
            "Kevin",
            "Jordy"}

student = input("Enter the name of the student: ")


if student not in students: 
    print(f"{student} was not found ")
else:
    print(f"{student} was found")


#Here is another example usign a dictionary


students_dictionary = {"Jossua" : "A",
            "Kevin" : "B",
            "Jordy" : "C",
            "Alison" : "D"}



student_dictionary = input("Enter the name of a student: ")

if student_dictionary in students_dictionary:
    print(f"{student_dictionary} grade is {students_dictionary[student_dictionary]}")
else: 
    print(f"{student_dictionary} was not found")

    
# The next example shows how can we check if an email is valid 

email = input("Enter your email: ")

if "@" in email and "." in email:
    print(f"{email} IS VALID")
else:
    (f"The email is not valid")

 
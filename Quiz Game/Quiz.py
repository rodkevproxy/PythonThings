#Python quiz game

questions = ("Best module on this year of uni",
             "Worst module on this year of uni",
             "Module that surprised you the most", 
             "Module that did not have any impact",
             "Module that you will take again" )

options = (("A. First Module", "B. Second Module", "C. Third Module", "D. Fourth Module "), 
           ("A. First Module", "B. Second Module", "C. Third Module", "D. Fourth Module "),
           ("A. First Module", "B. Second Module", "C. Third Module", "D. Fourth Module "),
           ("A. First Module", "B. Second Module", "C. Third Module", "D. Fourth Module "), 
           ("A. First Module", "B. Second Module", "C. Third Module", "D. Fourth Module "))

#Because i made a mistake while planning i decided to turn the quiz into a game about how much does my uni friends know about me

answers = ("B", "C", "C", "A", "D")
guesses = [] #This is a list because we need to append the names 
score = 0 
question_num = 0 

for question in questions: 
    print("---------------------------")
    print(question)
    for option in options[question_num]: 
        print(option)

    guess = input("Select (A, B, C, D): ").upper()
    guesses.append(guess)

    if guess == answers[question_num]:
        print("CORRECT!")
        score += 1 
    else: 
        print("INCORRECT")
        print(f"{answers[question_num]} is the correct option")
    question_num += 1 
print ("--------------------------")
print ("         RESULTS          ")
print ("--------------------------")

print("Answers: ",end=" " )
for answer in answers: 
    print (answer, end=" ")
print()


print("Guesses: ", end=" ")
for guess in guesses: 
    print(guess, end=" ")
print()

# Added this score method that prints the final score percentage 

score = int((score / len(questions) * 100)) #Typecaste the score varaible as an integer

print (f"Your total score was {score}%")



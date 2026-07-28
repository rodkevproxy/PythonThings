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


guesses = [] #This is a list because we need to append the names 
score = 0 
question_num = 0 


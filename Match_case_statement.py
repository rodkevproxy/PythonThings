# Match-Case statement (Switch): An alternative to using many elif statements 
#                                   Escecutes some code if a value matches a case 
#                                   Benefits: Cleared and syntax us more radable     


def day_of_week(day):
    match day: 
        case 1: 
            return "Monday"
        case 2: 
            return "Tuesday"
        case 3: 
            return "Wednesday"
        case 4: 
            return "Thursday"
        case 5: 
            return "Friday"
        case 6: 
            return "Saturday"
        case 7: 
            return "Sunday"#
        case _:    #The "_" acts as an else statement within the match case 
            return "Invalid input"


print (day_of_week("Pizza"))

# Alternative to many if-else statements 
# These cam be modified to avoid too many lines of code 



def weekend_day(w_day): 
    match w_day: 
        case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
            return False
        case "Sunday" | "Saturday":
            return True 
        case _: 
            return False 

print(weekend_day("Sunday"))





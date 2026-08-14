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


print (day_of_week(3))


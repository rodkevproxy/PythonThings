# This one will is set to continiue on sunday 
# 2D List is a list made out of lists


#This 2D collection is a Lists

groceries = [["Apple", "orange", "banana", "coconut"],
             ["celery", "carrots", "potatoes"],
             ["chicken", "fish", "turkey"]]

# This can be also tuples made os sets, or use different ones depending on what is bet for the program


for collection in groceries:
    for food in collection:
        print(food, end = " ")




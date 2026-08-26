# Classes can take a lot off space, so for better organization it is convinient to put them on separate files

class Car: 
    def __init__(self, model, year, colour, for_sale): #This is the constructor method, this is required in order to construct objects 
        self.model = model 
        self.year = year
        self.colour = colour 
        self.for_sale = for_sale 

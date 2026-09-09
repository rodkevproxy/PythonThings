# Magic Methods = Dunder methods (Double undescore) __init__, __str__,__eq__
#                 They are automatically called by mmany of Python's built in operations
#                 They allow developers to define or customize the behavior of objects 


class Book: 
    def __init__(self, title, author, num_pages):
        self.title = title 
        self.author = author 
        self.num_pages = num_pages

    def __str__(self):  #This method will change the message given whne printing an object 
        return f"'{self.title}' by {self.author}"
    
    def __eq__(self, other): #This method will return if 2 "books in this case" are equal
        return self.title == other.title and self.author == other.author
    
    def __lt__(self, other): #Basically this allow python to compare two objects using the "<"  symbol 
        return self.num_pages < other.num_pages
    
    def __lt__(self, other): #Basically this allow python to compare two objects using the "<"  symbol 
        return self.num_pages > other.num_pages

    def __add__(self, other): #This funtion will allow the addition between the number of pages of each object ("Book")
        return f"{self.num_pages} + {other.num_pages} pages"

    def __contains__(self, keyword):
        return keyword in self.title or self.author 
    def __getitem__(self, key):
        if key == "Author":
            return self.author
        elif key == "Title":
            return self.title
        elif key == self.num_pages: 
            return self.num_pages
        else: 
            return f"The key {key} was not found"

        
        




book1 = Book("neetCode", "The Neet Code Guy", 330) #Lets pretend i did create like 2 other objects similar to this 
book2 = Book("The oddysey", "The Guy", 330)

print(book2)
print(book1 < book2)
print(book1 == book2)
print(book1 + book2)
print("oddysey" in book2)
print(book1["Author"])
print(book1["Title"])
print(book1["Audio"])

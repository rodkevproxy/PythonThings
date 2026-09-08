# Magic Methods = Dunder methods (Double undescore) __init__, __str__,__eq__
#                 They are automatically called by mmany of Python's built in operations
#                 They allow developers to define or customize the behavior of objects 


class Book: 
    def __init__(self, title, author, num_pages):
        self.title = title 
        self.author = author 
        self.num_pages = num_pages

    def __str__(self):
        return f"'{}' by {}"


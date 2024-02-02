# Python Object Oriented Programming by Joe Marini course example
# Using instance methods and attributes


class Book:
    # the "init" function is called when the instance is
    # created and ready to be initialized
    def __init__(self, title, author, pages, price):
        self.title = title
        self.author = author
        self.pages = pages
        self.price = price
        self.__secret = "Secret attribute!!!"

    def getPrice(self):
        if hasattr(self, "_discount"): # hasattr checks if that attribute is set for that instance
            return self.price - (self.price * self._discount)
        else:
            return self.price
    
    def setDiscount(self, amount):
        self._discount = amount

# TODO: create some book instances
b1 = Book("War and Peace", "Me", 200, 11)
b2 = Book("The Catcher in the Rye", "You", 1000, 25)

# TODO: print the price of book1
print(b1.getPrice())

# TODO: try setting the discount
print(b2.getPrice())
b2.setDiscount(0.25)
print(b2.getPrice())

# TODO: properties with double underscores are hidden by the interpreter
print(b2.__secret)
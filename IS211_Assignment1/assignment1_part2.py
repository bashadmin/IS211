
class Book:
    def __init__(self, author, title):
        self.title = title 
        self.author = author
    
    def display(self):
        print("{}, written by {}".format
        (self.title,self.author))


if __name__ == "__main__":
    theHobbit = Book("J.R.R Tolken", "The Two Towers")
    theHobbit.display()


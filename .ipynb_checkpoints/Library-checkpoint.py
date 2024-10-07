#create class and methods
class Book:
    def __init__(self, title, author, year, price, stoplist, genre):
        self.title = title
        self.author = author
        self.year = year
        self.price = price
        self.stoplist = stoplist
        self.genre = genre

    def get_info(self):
        print(f"Author: {self.author}")
        print(f"Title: {self.title}")
        print(f"Year: {self.year}")
        print(f"Price: {self.price}")
        print(f"Stoplist: {self.stoplist}")
        print(f"Genre: {self.genre}")

    def set_stoplist(self, boolean):
        self.stoplist = boolean

    def censor(self, author_name, boolean):
        if self.author == author_name:
            self.stoplist = boolean

def find_most_expensive_book(books):
    most_expensive = books[0]
    for book in books:
        if book.price > most_expensive.price:
            most_expensive = book
    return most_expensive
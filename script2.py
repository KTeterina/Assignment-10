import Library

book1 = Library.Book("The Lord of the Rings", "J.R.R. Tolkien", 1954, 1138, False, "Fantasy")
book2 = Library.Book("Harry Potter and the Philosopher's Stone", "J. K. Rowling", 1997, 1026, True, "Fantasy")
book3 = Library.Book("The Master and Margarita", "Mikhail Bulgakov", 1973, 513, False, "Fantasy Romance")
book4 = Library.Book("To Kill a Mockingbird", "Harper Lee", 1960, 442, False, "Historical Fiction")

books = [book1, book2, book3, book4]

# Run class methods for individual books
print("Book 1 Information:")
book1.get_info()
book1.set_stoplist(True)
print("Book 1 Stoplist set to True")

print("\nBook 2 Information:")
book2.get_info()
book2.censor("J. K. Rowling", False)
print("Book 2 Stoplist set to False")

# Run class methods for the list of books
print("\nMost Expensive Book:")
most_expensive_book = Library.find_most_expensive_book(books)
if most_expensive_book:
    most_expensive_book.get_info()
else:
    print("No books in the list.")
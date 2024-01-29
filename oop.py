class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book.title}' by {book.author} added to the library.")

    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)
            print(f"Book '{book.title}' by {book.author} removed from the library.")
        else:
            print("Book not found in the library.")

    def display_books(self):
        if not self.books:
            print("The library is empty.")
        else:
            print("Books in the library:")
            for book in self.books:
                print(f"Title: {book.title}, Author: {book.author}, ISBN: {book.isbn}")


book1 = Book("1984", "George Orwell", "9780151660346")
book2 = Book("Midnight in Chernobyl", "Adam Higginbotham", "9780552172899")

library = Library()

library.remove_book(book1)
library.add_book(book2)

library.display_books()

library.remove_book(book2)

library.display_books()
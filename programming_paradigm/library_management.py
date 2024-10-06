# library_management.py

class Book:
    def __init__(self, title, author):
    
        self.title = title
        self.author = author
        self._is_checked_out = False  # Private attribute to track if the book is checked out

    def check_out(self):
        
        self._is_checked_out = True

    def return_book(self):
        
        self._is_checked_out = False

    def is_available(self):
        
        return not self._is_checked_out


class Library:
    def __init__(self):
        
        self._books = []  # Private list to store books

    def add_book(self, book):
       
        self._books.append(book)

    def check_out_book(self, title):
        
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                print(f"Checked out: '{title}'")
                return
        print(f"'{title}' is not available for checkout.")

    def return_book(self, title):
        
        for book in self._books:
            if book.title == title and not book.is_available():
                book.return_book()
                print(f"Returned: '{title}'")
                return
        print(f"'{title}' is not currently checked out.")

    def list_available_books(self):
        
        available_books = [book for book in self._books if book.is_available()]
        if not available_books:
            print("No books are currently available.")
        else:
            for book in available_books:
                print(f"{book.title} by {book.author}")



class Book:
    def __init__(self, title : str, author : str) -> None:
        self.title = title
        self.author = author
        
    def __str__(self):
        return f"Book: {self.title} by {self.author}"
             
class EBook(Book):
    def __init__(self, title: str, author: str, file_size : int) -> None:
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self) -> str:
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"

class PrintBook(Book):
    def __init__(self, title: str, author: str, page_count : int) -> None:
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self) -> str:
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"

class Library:
    def __init__(self) -> None:
        self.books = []

    def add_book(self, book):
        return self.books.append(book)

    def list_books(self):
        for book in self.books:
            print(book)


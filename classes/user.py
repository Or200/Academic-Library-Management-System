from .book import Book

class User:

    def __init__(self, user_id: int, user_name: str):
        self.user_id = user_id
        self.user_name = user_name
        self.borrowed_books = []
        
    def borrow_book(self, book: Book) -> None:
        self.borrowed_books.append(book)

    def return_book(self, book: Book) -> None:
        self.borrowed_books.remove(book)

   
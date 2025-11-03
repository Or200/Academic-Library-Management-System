from .user import User
from .book import Book
from .logger import Logger
from .systemAdmin import SystemAdmin

class Library:

    max_borrow_days: int = 14

    def __init__(self):
        self.books: dict[str, Book] = {}
        self.users: dict[str, User] = {}

    def register_user(self, user: User) -> None:
        self.users[user.user_id] = user

    def add_book(self, book: Book) -> None:
        self.books[book.book_id] = book

    def perform_borrow(self, user_id: int, book_id: int) -> None:
        if user_id in self.users:
            if book_id in self.books:
                user = self.users[user_id]
                book = self.books[book_id]
                if book.is_available:
                    user.borrow_book(book)
                    book.is_available = False
                    Logger.log_action("BORROW", f"user id: {user_id}, book id: {book_id}.")
                    SystemAdmin.update_transactions_count()

                else:
                    print("book not available")
            else:
                print("book not exist")
        else:
            print("user not exist")

    def perform_return(self, user_id: int, book_id: int) -> None:
        if user_id in self.users:
            if book_id in self.books:
                user = self.users[user_id]
                book = self.books[book_id]
                if not book.is_available:
                    if book in user.borrowed_books :
                        user.return_book(book)
                        book.is_available = True
                        Logger.log_action("RETURN", f"user id: {user_id}, book id: {book_id}.")
                        SystemAdmin.update_transactions_count()

                    else:
                        print(f"book not exist in user {user.user_name}")
                else:
                    print("not return - book available")
            else:
                print("book not exist")
        else:
            print("user not exist")


    
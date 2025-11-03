from classes.book import Book
from classes.user import User
from classes.library import Library
from classes.systemAdmin import SystemAdmin
from classes.logger import Logger

if __name__ == "__main__":
    book1 = Book("harry potter 1", "J.K. Rowling - hp1")
    book2 = Book("harry potter 2", "J.K. Rowling - hp2")
    book3 = Book("harry potter 3", "J.K. Rowling - hp3")
    user1 = User(123456789, "Israel Israeli")
    user2 = User(987654321, "Yossef Yossi")
    my_library = Library()
    my_library.add_book(book1)
    my_library.add_book(book2)
    my_library.add_book(book3)
    my_library.register_user(user1)
    my_library.register_user(user2)
    my_library.perform_borrow(123456789, 1000)
    my_library.perform_borrow(123456789, 1001)
    my_library.perform_borrow(987654321, 1002)
    print(my_library.users[123456789].borrowed_books)
    my_library.perform_return(123456789, 1000)


    Logger.log_action("EXIT", "-------------------------")

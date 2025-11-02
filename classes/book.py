class Book:

    count = 1000

    def __init__(self, title: str, author: str, is_available: bool = True):
        self.title = title
        self.author = author
        self.is_available = is_available
        self.book_id = Book.count

        Book.count += 1
    
    def get_details1(self) -> str:
        if self.is_available:
            x = ""
        else:
            x = "not "
            
        return f"The book {self.title} write by {self.author}. book id is {self.book_id} and is {x}available to broww"
    
    def get_details(self) -> str:
            return f"The book {self.title} write by {self.author}. book id is {self.book_id}"


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_available = True

   
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def check_out_book(self, title):
        for book in self.books:
            if book.title == title and book.is_available:
                book.is_available = False
                return True
        return False
    
    def return_book(self):
        for book in self.books:
            if book.title ==  book.is_available:
                book.is_available = True
                return True
        return False
    
    def list_available_books(self):
        available_books =[]
        for book in self.books:
            if book.is_available:
                available_books.append(book.title)
        return available_books
 

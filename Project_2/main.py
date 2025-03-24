class Book:
    def __init__(self, title, author, available=True):
        self.title = title
        self.author = author
        self.available = available
        
class Library:
    def __init__(self):
            self.books = []
            
    def add_book(self, book):
        self.books.append(book)
        print(f"{book.title} telah ditambahkan")
        
    def borrow_book(self, title):
        for book in self.books:
            if book.title == title and book.available:
                book.available = False
                print(f"{title} telah dipinjam")
                return
        print(f"{title}  sedang dipinjam")
        
    def return_book(self, title):
        for book in self.books:
            if book.title == title and not book.available:
                book.available = True
                print(f"{title} telah dikembalikan")
                return
        print(f"{title} tidak ditemukan atau belum dipinjam")
        
library = Library()

book1 = Book("Python OOP", "author A")
book2 = Book("Machine Learning", "author B")

library.add_book(book1)
library.add_book(book2)

library.borrow_book("Python OOP")
library.borrow_book("Machine Learning")

library.return_book("Python OOP")
library.return_book("Machine Learning")
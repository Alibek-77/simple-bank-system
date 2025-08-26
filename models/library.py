from book import Book
from user import User
class Library:
    def __init__(self):
        self.books=[]
        self.users=[]
    def add_book(self,book):
        self.books.append(book)
    def add_user(self,user):
        self.users.append(user)
    def list_books(self):
        for book in self.books:
            status='Bar' if not book.is_borrowed else 'Alynyp koygan'
            print(f"{book.title}-{book.author}({status})")
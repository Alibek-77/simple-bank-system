from library import Library
from book import Book
from user import User
lib=Library()
book1=Book('Python basics','Gido van Rossum')
book2=Book('Flask Web Dev','Miguel Grinberg')
lib.add_book(book1)
lib.add_book(book2)
user1=User('Alibek')
lib.add_user(user1)
print('Kitaptar')
lib.list_books()
print('\n Alibek kitap alyp zhatyr ...')
user1.borrow_book(book2)
print('\n Kitaptar:')
lib.list_books()
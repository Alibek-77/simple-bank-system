class Book():
    def __init__(self,title,author):
        self.title=title
        self.author=author
        self.is_borrowed=False
    def borrow(self):
        if self.is_borrowed:
            raise Exception('Bul kitap kazir zhok!')
        self.is_borrowed=True
    def return_book(self):
        self.is_borrowed=False

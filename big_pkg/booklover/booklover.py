import pandas as pd

class BookLover:
    
    def __init__(self, name, email,fav_genre):
        self.num_books = 0
        self.book_list = pd.DataFrame(columns=['book_name','rating'])
        self.name = name
        self.email = email
        self.fav_genre = fav_genre
        
    def add_book(self, book_name, rating):
        new_book = {'book_name': [book_name], 'rating': [rating]}
        new_book_df = pd.DataFrame(new_book)
        if 'book_name' in self.book_list.columns and book_name in self.book_list['book_name'].values:
            print('This book is already in your list.')
        else:
            self.book_list = pd.concat([self.book_list, new_book_df], ignore_index=True)
            self.num_books += 1
            
    def has_read(self, book_name):
        if book_name in self.book_list['book_name'].values:
            print('True')
        else:
            print('False')
            
    def num_books_read(self):
        return self.num_books
    
    def fav_books(self):
        return self.book_list[self.book_list['rating'] > 3]
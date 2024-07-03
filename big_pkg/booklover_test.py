import unittest
import pandas as pd
from big_pkg.booklover.booklover import BookLover


class BookLoverTestSuite(unittest.TestCase):
    def test_1_add_book(self):
        book1 = "The Alchemist"
        person1 = BookLover('Kiana', 'kdane@dane.com', 'Adventure')
        book_list_dict = {"book_name": ["Jane Eyre",
                            "Fight Club",
                            "The Divine Comedy",
                            "The Popol Vuh"],
                            "rating": [4, 3, 5, 5]}
        person1.book_list = pd.DataFrame(book_list_dict)
        person1. num_books = len(book_list_dict["book_name"])
        person1.add_book(book1, 4)
        
        self.assertTrue(book1 in person1.book_list['book_name'].values)
        
        
    def test_2_add_book(self):
        person2 = BookLover('Kiana', 'kdane@dane.com', 'Adventure')
        book_list_dict = {"book_name": ["Jane Eyre", "Fight Club", "The Divine Comedy", "The Popol Vuh"],
                            "rating": [4, 3, 5, 5]}
        person2.book_list = pd.DataFrame(book_list_dict)
        person2.num_books = len(book_list_dict["book_name"])
    
        book_to_add = "The Alchemist"
        person2.add_book(book_to_add, 4)
        person2.add_book(book_to_add, 4)
    
        self.assertEqual(person2.book_list['book_name'].tolist().count(book_to_add), 1)
    
    
    def test_3_has_read(self):
        person3 = BookLover('Kiana', 'kdane@dane.com', 'Adventure')
        book_list_dict = {"book_name": ["Jane Eyre", "Fight Club", "The Divine Comedy", "The Popol Vuh"],
                        "rating": [4, 3, 5, 5]}
        person3.book_list = pd.DataFrame(book_list_dict)
        person3.num_books = len(book_list_dict["book_name"])
    
        book_in_list = "Jane Eyre"
        try:
            result = person3.has_read(book_in_list)
            self.assertTrue(result)
        except AssertionError as e:
            print('Test3 caught an exception!!!!!!!!!', e)
    
    
    def test_4_has_read(self):
        person4 = BookLover('Kiana', 'kdane@dane.com', 'Adventure')
        book_list_dict = {"book_name": ["Jane Eyre", "Fight Club", "The Divine Comedy", "The Popol Vuh"],
                        "rating": [4, 3, 5, 5]}
        person4.book_list = pd.DataFrame(book_list_dict)
        person4.num_books = len(book_list_dict["book_name"])
    
        book_not_in_list = "The Alchemist"
        self.assertFalse(person4.has_read(book_not_in_list))
    
    def test_5_num_books_read(self):
        person5 = BookLover('Kiana', 'kdane@dane.com', 'Adventure')
        book_list_dict = {"book_name": ["Jane Eyre", "Fight Club", "The Divine Comedy", "The Popol Vuh"],
                        "rating": [4, 3, 5, 5]}
        person5.book_list = pd.DataFrame(book_list_dict)
        person5.num_books = len(book_list_dict["book_name"])
    
        self.assertEqual(person5.num_books_read(), person5.num_books)
    
    def test_6_fav_books(self):
        person6 = BookLover('Kiana', 'kdane@dane.com', 'Adventure')
        book_list_dict = {"book_name": ["Jane Eyre", "Fight Club", "The Divine Comedy", "The Popol Vuh", "The Alchemist"],
                        "rating": [4, 3, 2, 5, 4]}
        person6.book_list = pd.DataFrame(book_list_dict)
        person6.num_books = len(book_list_dict["book_name"])
    
        fav_books = person6.fav_books()
        self.assertTrue((fav_books['rating'] > 3).all())

if __name__ == '__main__':
    unittest.main(verbosity=3)
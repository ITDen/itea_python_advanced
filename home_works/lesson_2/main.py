from home_works.lesson_2.library import Library
from home_works.lesson_2.person import Person
from home_works.lesson_2.book import Book

user_1 = Person('Den', 30)
user_2 = Person('Ivan', 23)
user_3 = Person('Nik', 43)

book_1 = Book(1, 'C book #1', 'B author1', 2006)
book_2 = Book(2, 'Y book #2', 'G author2', 2005)
book_3 = Book(3, 'F book #3', 'Z author3', 2001)

library = Library()
library.add_book(book_3)
library.add_book(book_2)
library.add_book(book_1)

library.get_all_books(sort='year')
print('=============================')

library.assign_book(user_1, book_2)
library.assign_book(user_2, book_1)
print('=============================')

print('Books in use')
user_1.books_in_use()
user_2.books_in_use()
user_3.books_in_use()
print('=============================')

# library.get_available_books()
# library.get_unavailable_books()
# print('=============================')

library.get_available_books()
library.unassign_book(user_1, book_2)
print('=============================')

library.get_available_books()
library.unassign_book(user_2, book_1)
print('=============================')
library.get_available_books(sort='name')
library.del_book(book_1)
library.del_book(book_2)
library.del_book(book_3)
library.get_available_books(sort='name')

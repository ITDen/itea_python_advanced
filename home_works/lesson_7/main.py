from home_works.lesson_7.utils.server import SocketServer
from home_works.lesson_7._library.library import Library
from home_works.lesson_7._library.book import Book
from home_works.lesson_7._library.person import Person

'''
Сервер и библиотека запускаются из main файла, клиент из файла client & client2
в Library добавил Event на добавление/удаление книг 
'''
if __name__ == '__main__':
    # Read all books and make books obj list
    with open('_library/books.txt', 'r') as f:
        books = [Book(int(book[0]), book[1], book[2], int(book[3])) for raw_book in f.readlines()
                 for book in [raw_book.strip().split(',')]]

    # # make library object and add books
    library = Library()
    for book in books: library.add_book(book)
    print('Library created!')
    print('===========================')

    user_1 = Person('Den', 30)
    user_2 = Person('Ivan', 23)
    user_3 = Person('Nik', 43)

    book_1 = Book(1, 'C book #1', 'B author1', 2006)
    book_2 = Book(2, 'Y book #2', 'G author2', 2005)
    book_3 = Book(3, 'F book #3', 'Z author3', 2001)

    library.add_book(book_3)
    library.add_book(book_2)
    library.add_book(book_1)

    library.assign_book(user_1, book_2)
    library.assign_book(user_2, book_1)

    print('=============================')
    print()

    # Start server for initialized library
    SocketServer(library=library)
    print()

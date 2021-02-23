from home_works.lesson_6.utils.server import SocketServer
from home_works.lesson_6._library.library import Library
from home_works.lesson_6._library.book import Book

'''
Сервер и библиотека запускаются из main файла, клиент из файла client
'''
if __name__ == '__main__':
    # Read all books and make books obj list
    with open('_library/books.txt', 'r') as f:
        books = [Book(int(book[0]), book[1], book[2], int(book[3])) for raw_book in f.readlines()
                 for book in [raw_book.strip().split(',')]]

    # make library object and add books
    library = Library()
    for book in books: library.add_book(book)
    print('Library created!')
    print('===========================')

    print()
    # Start server for initialized library
    SocketServer(library=library)

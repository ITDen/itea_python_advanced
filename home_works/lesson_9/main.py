from home_works.lesson_9.library_client import *
import psycopg2 as psql

if __name__ == '__main__':
    connection = psql.connect('postgresql://test_user:rfhnjxrf67@192.168.122.239/test_db')
    library = Library(connection)

    # library.add_books_from_file('itea_library/books.txt')
    LibraryClient(library=library)

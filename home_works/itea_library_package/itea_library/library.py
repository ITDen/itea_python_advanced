from itea_library.book import Book
from itea_library.person import Person
from threading import Event
from time import sleep


class Library:
    """Class which describe library"""

    def __init__(self):
        self.__books = []
        self.__persons = []
        self.__book_event = Event()

    def get_member_list(self) -> list:
        """
        Method return list of all library members
        :return: sorted list
        """
        return self.__persons

    def get_all_books(self, sort: str = 'year') -> list:
        """
        Method return sorted(default by year) list of all books in library
        :param sort: use one of sort key 'name, author, year - default'
        :return: sorted list
        """
        books = sorted(self.__books, key=lambda book: book.__getattribute__(sort))
        # for book in books:
        #     print(book)
        return books

    def get_available_books(self, sort: str = 'year') -> list:
        """
        Method return sorted(default by year) list of available books in library
        :param sort: use one of sort key 'name, author, year - default'
        :return: sorted list
        """
        books = sorted([book for book in self.__books if not book.in_use()],
                       key=lambda book: book.__getattribute__(sort))
        # for book in books:
        #     print(book)
        return books

    def get_unavailable_books(self, sort: str = 'year') -> list:
        """
        Method return sorted(default by year) list of unavailable books in library
        :param sort: use one of sort key 'name, author, year'
        :return: sorted list
        """
        books = sorted([book for book in self.__books if book.in_use()], key=lambda book: book.__getattribute__(sort))
        # for book in books:
        #     print(book)
        return books

    def add_book(self, book: Book) -> None:
        """
        Method add book to library
        :param book:
        :return: None
        """
        # Event for block adding book if some book deleting at same time
        if not self.__book_event.is_set():
            if book not in self.__books:
                self.__book_event.set()
                self.__books.append(book)
                # sleep(5)
                self.__book_event.clear()
                print(f'Book {book} has been added to library!')
            else:
                print(f'Book {book} already in library!')
        else:
            print(f'Please try later!')

    def del_book(self, book: Book) -> None:
        """
        Method delete book from library
        :param book: Book
        :return: None
        """
        # Event for block removing used book
        if not self.__book_event.is_set():
            if book in self.__books:
                self.__book_event.set()
                self.__books.pop(self.__books.index(book))
                # sleep(5)
                self.__book_event.clear()
                print(f'Book {book} has been deleted from library!')
            else:
                print(f'Book {book} not found')
        else:
            print(f'Please try later!')

    def assign_book(self, person: Person, book: Book) -> bool:
        """
        Method assign book to person
        :param person: Person
        :param book: Book
        :return: None
        """
        if book not in self.__books:
            print(f'Sorry, book {book} not found!')
            return False
        else:
            if person.assign_book(book) and book.assign_user(person):
                if person not in self.__persons:
                    self.__persons.append(person)
                print(f'Book {book} was given to {person}!')
            else:
                print(f'Something goes wrong while assigning book!')
                return False

    def unassign_book(self, person: Person, book: Book) -> bool:
        """
        Method unassign book from person
        :param person: Person
        :param book: Book
        :return: None
        """
        if book not in self.__books:
            print(f'Sorry, book {book} not found!')
            return False
        elif person not in self.__persons:
            print(f'User {person} are not library member!')
            return False
        else:
            if person.unassign_book(book) and book.unassign_user(person):
                print(f'Book {book} returned in library from {person}')
                return True
            else:
                print(f'Something goes wrong while unassigning book {book} from person {person}!')
                return False

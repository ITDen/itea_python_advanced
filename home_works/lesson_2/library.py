'''
Библиотека

Создать три класса:
1. Класс библиотека
    Поля:
        - список книг (list Books)
        - список читателей (list Readers)

    Методы:
        - Добавить книгу
        - Удалить книгу
        - Отдать книгу читателю
        - Принять книгу от читателя

        - Вывести список всех книг
        - Вывести список книг в библиотеке (в наличии)
        - Вывести списк книг, которые не в наличии

        - Отсортировать список книг по названию, автору, году издания (lambda будет плюсом)
'''
from book import Book
from person import Person


class Library:
    """Class which describe library"""

    def __init__(self):
        self.__books = []
        self.__persons = []

    def get_all_books(self, sort: str = 'year') -> list:
        """
        Method return sorted(default by year) list of all books in library
        :param sort: use one of sort key 'name, author, year - default'
        :return: sorted list
        """
        for book in sorted(self.__books, key=lambda book: book.__getattribute__(sort)):
            print(book)
        return self.__books

    def get_available_books(self, sort: str = 'year') -> list:
        """
        Method return sorted(default by year) list of available books in library
        :param sort: use one of sort key 'name, author, year - default'
        :return: sorted list
        """
        books = sorted([book for book in self.__books if not book.in_use()],
                       key=lambda book: book.__getattribute__(sort))
        for book in books:
            print(book)
        return books

    def get_unavailable_books(self, sort: str = 'year') -> list:
        """
        Method return sorted(default by year) list of unavailable books in library
        :param sort: use one of sort key 'name, author, year'
        :return: sorted list
        """
        books = sorted([book for book in self.__books if book.in_use()], key=lambda book: book.__getattribute__(sort))
        for book in books:
            print(book)
        return books

    def add_book(self, book: Book) -> None:
        """
        Method add book to library
        :param book:
        :return: None
        """
        if book not in self.__books:
            self.__books.append(book)
            print(f'Book {book} has been added to library!')
        else:
            print(f'Book {book} already in library!')

    def del_book(self, book: Book) -> None:
        """
        Method delete book from library
        :param book: Book
        :return: None
        """
        if book in self.__books:
            self.__books.pop(self.__books.index(book))
            print(f'Book {book} has been deleted from library!')
        else:
            print(f'Book {book} not found')

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

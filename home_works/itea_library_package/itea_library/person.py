class Person:
    """Class which describe library subscriber"""
    def __init__(self, name: str, age: int):
        self.__name = name
        self.__age = age
        self.__books = []

    def assign_book(self, book) -> bool:
        """
        Method add book to person use list
        :param book: Book
        :return: bool
        """
        if book not in self.__books:
            self.__books.append(book)
            return True
        else:
            # print(f'{book} already in use in {self}')
            return False

    def unassign_book(self, book) -> bool:
        """
        Method remove book from person use list
        :param book: Book
        :return: bool
        """
        if book in self.__books:
            self.__books.pop(self.__books.index(book))
            return True
        else:
            # print(f'{self} not use {book}')
            return False

    def books_in_use(self, sort: str = 'year') -> list or None:
        """
        Method return person book's use list
        :param sort: use one of sort key 'name, author, year - default'
        :return: sorted list
        """
        books = sorted([book for book in self.__books], key=lambda book: book.__getattribute__(sort))
        if books:
            print(f'{self} has in use next books:')
            for book in books:
                print(book)
            return books
        else:
            print(f'{self} has no books in use!')

    def __str__(self):
        return f'Name: {self.__name}, age: {self.__age}'

    def __repr__(self):
        return f'{self.__name}, {self.__age}'

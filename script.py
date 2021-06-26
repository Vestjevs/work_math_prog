class Library:
    def __init__(self):
        self.__authors = []
        self.__books = []

    def add_book(self, book):
        self.__books.append(book)
        self.__authors.append(book.get_author())

    def is_book_present(self, name):
        for i in range(0, len(self.__books)):
            if self.__books[i].get_name() == name:
                return i
        return -1

    def get_book(self, name):
        i = self.is_book_present(name)
        if i is not -1:
            return self.__books[i]


class Book:
    def __init__(self, author, name=''):
        self.__name = name
        self.__author = author

    def get_name(self):
        return self.__name

    def get_author(self):
        return self.__author

    def get_author_name(self):
        return self.__author.get_name()


class Author:
    def __init__(self, name=''):
        self.__name = name
        self.__bio = ''

    def set_bio(self, bio):
        self.__bio = bio

    def get_name(self):
        return self.__name

    def get_bio(self):
        return self.__bio


if __name__ == '__main__':
    pass

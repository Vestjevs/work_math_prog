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
        if i != -1:
            return self.__books[i]

    def delete_book(self, name):
        i = self.is_book_present(name)
        if i != -1:
            self.__books.pop(i)

    def show_books(self):
        print('\n'.join([f"Автор: {elem.get_author().get_name()}, название: {elem.get_name()}" for elem in self.__books]))

    def author_search(self, name):
        result = self.is_author_present(name)
        if result != -1:
            print("\n".join([elem for elem in self.__books if elem.get_author().get_name() == name]))

    def show_books_by_author(self, name):
        book_list_by_author = []
        for i in range(0, len(self.__books)):
            if self.__books[i].get_author().get_name() == name:
                book_list_by_author.append(self.__books[i].get_name())
        print("\n".join(book_list_by_author))


    def is_author_present(self, name):
        for i in range(0, len(self.__authors)):
            if self.__authors[i].get_name() == name:
                return i
        return -1

    def delete_author(self, name):
        result = self.is_author_present(name)
        if result != -1:
            book_delete_list = [elem for elem in self.__books if elem.get_author().get_name() == name]
            for book in book_delete_list:
                self.__books.remove(book)
            self.__authors.pop(result)


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

    def __str__(self):
        return self.__name


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
    my_library = Library()
    pattern = "1. Лев Толстой «Война и мир»\n" \
              "2. Джордж Оруэлл «1984»\n" \
              "3. Джеймс Джойс «Улисс»\n" \
              "4. Владимир Набоков «Лолита»\n" \
              "5. Уильям Фолкнер «Звук и ярость»"

    book_author_list = pattern.split('\n')
    for entry in book_author_list:
        aux = entry.split('«')
        book = Book(Author(str(aux[0])[3:-1]), str(aux[1])[0:-1])
        my_library.add_book(book)

    my_library.show_books()


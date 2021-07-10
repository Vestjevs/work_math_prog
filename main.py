import pandas as pd
import library as lib


def get_dataset(path):
    return pd.read_csv(path)


library_all = lib.Library()
ds = get_dataset(r'C:\Users\Lenovo\Downloads\books_csv.csv')
for book, author in zip(list(ds['title']), list(ds['authors'])):
    new_book = lib.Book(author=lib.Author(author), name=book)
    library_all.add_book(new_book)



if __name__ == '__main__':
    library_all.show_books_by_author('J.K. Rowling/Mary GrandPrГ©')
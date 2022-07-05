class Serializable:
    pass


class CSVMixin:
    pass


class JSONMixin:
    pass


class XMLMixin:
    pass


class Book(CSVMixin, Serializable):
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price


if __name__ == '__main__':
    b = Book("Practice Makes Python", "Reuven Lerner", 39)
    b.dump('book.csv')

    b2 = Book('blah title', 'blah author', 100)
    b2.load('book.csv')

    print(f'Title: {b2.title}\n'
          f'Author: {b2.author}\n'
          f'Price: {b2.price}\n')

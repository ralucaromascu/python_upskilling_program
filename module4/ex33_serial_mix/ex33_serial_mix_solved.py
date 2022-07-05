import pickle
import csv
import json
from xml.etree import ElementTree as ET


class Serializable(object):
    def dump(self, filename):
        pickle.dump(vars(self),
                    open(filename, 'wb'))

    def load(self, filename):
        old_vars = pickle.load(open(filename, 'rb'))

        for name, value in old_vars.items():
            setattr(self, name, value)


class JSONMixin(object):
    def dump(self, filename):
        json.dump(vars(self),
                  open(filename, 'w'))

    def load(self, filename):
        old_vars = json.load(open(filename, 'r'))

        for name, value in old_vars.items():
            setattr(self, name, value)


class CSVMixin(object):
    def dump(self, filename):
        with open(filename, 'w', newline='') as csvfile:
            o = csv.writer(csvfile, delimiter='\t')
            for name, value in vars(self).items():
                o.writerow([name, value])

    def load(self, filename):
        with open(filename, 'r', newline='') as csvfile:
            i = csv.reader(csvfile, delimiter='\t')
            for name, value in i:
                setattr(self, name, value)


class XMLMixin(object):
    def dump(self, filename):
        a = ET.Element('attributes')
        for name, value in vars(self).items():
            node = ET.SubElement(a, name, value=str(value))

        tree = ET.ElementTree(a)

        with open(filename, 'wb') as xmlfile:
            tree.write(xmlfile)

    def load(self, filename):
        tree = ET.parse(open(filename, 'rb'))
        for parent in tree.iter():
            for child in parent:
                setattr(self, child.tag, child.attrib['value'])


if __name__ == '__main__':
    class Book(JSONMixin, Serializable):
        def __init__(self, title, author, price):
            self.title = title
            self.author = author
            self.price = price

        def __repr__(self):
            return f"{self.title}, by {self.author}, for {self.price}"


    b = Book("Python Workout", "Reuven Lerner", 39)
    print(b)
    b.dump('/tmp/book.data')

    b2 = Book('blah title', 'blah author', 100)
    # title, author, and price now reflect disk file
    b2.load('/tmp/book.data')
    print(b2)

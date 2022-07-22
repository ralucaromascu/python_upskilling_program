import argparse
my_file = None


class Head(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        if values is None:
            values = 3
        print(f'Here I am, setting the values {values} for the {option_string} option.. from file {my_file}.')
        setattr(namespace, self.dest, values)
        print(namespace)


class Tail(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        if values is None:
            values = 3
        print('Here I am, setting the values %r for the %r option...' % (values, option_string))
        setattr(namespace, self.dest, values)


def headtail():
    my_parser = argparse.ArgumentParser()
    my_parser.add_argument('-f', '--file', help="file to read", dest="file")

    my_parser.add_argument('-s', '--start', help="number of lines to read from head of the file", action=Head, nargs='?')
    my_parser.add_argument('-e', '--end', help="number of lines to read from head of the file", action=Tail, nargs='?')

    args = my_parser.parse_args()
    global my_file
    my_file = args.file
    print(my_file)


if __name__ == '__main__':
    headtail()

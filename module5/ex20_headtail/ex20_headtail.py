import argparse


def head(given_file, nr_lines):
    print(f'first {nr_lines} from {given_file}')


def tail(given_file, nr_lines):
    print(f'last {nr_lines} from {given_file}')


def headtail():
    my_parser = argparse.ArgumentParser()
    my_parser.add_argument('-f', '--file', help="file to read", nargs=1, required=True)

    my_parser.add_argument('-s', '--start', help="number of lines to read from head of the file", nargs='?', const=3,
                           type=int)
    my_parser.add_argument('-e', '--end', help="number of lines to read from head of the file", nargs='?', const=3,
                           type=int)

    args = my_parser.parse_args()
    if args.start:
        head(args.file, args.start)
    if args.end:
        tail(args.file, args.end)


if __name__ == '__main__':
    headtail()

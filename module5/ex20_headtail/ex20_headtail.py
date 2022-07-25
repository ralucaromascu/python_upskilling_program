import argparse
import os


def head(given_file, nr_lines):
    print(f'First {nr_lines} from {os.path.basename(given_file)}:')
    with open(given_file, 'r') as f:
        lines = f.readlines()
    print(*lines[:nr_lines], sep='')


def tail(given_file, nr_lines):
    print(f'Last {nr_lines} from {os.path.basename(given_file)}:')
    with open(given_file, 'r') as f:
        lines = f.readlines()
    print(*lines[-nr_lines:], sep='')


def headtail():
    my_parser = argparse.ArgumentParser()
    my_parser.add_argument('-f', '--file', help="file to read", required=True, type=str)

    my_parser.add_argument('-s', '--start', help="number of lines to read from head of the file", nargs='?', const=3,
                           type=int)
    my_parser.add_argument('-e', '--end', help="number of lines to read from head of the file", nargs='?', const=3,
                           type=int)

    args = my_parser.parse_args()
    print(args)
    if args.start:
        head(args.file, args.start)
    if args.end:
        tail(args.file, args.end)


if __name__ == '__main__':
    headtail()

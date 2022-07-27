import argparse
import os


def positive_int(nr):
    try:
        integer = int(nr)
    except:
        raise argparse.ArgumentTypeError('values for arguments -s/--start and -e/--end should be integer numbers')
    if integer <= 0:
        raise argparse.ArgumentTypeError('values for arguments -s/--start and -e/--end should be positive numbers')
    return integer


def headtail():
    my_parser = argparse.ArgumentParser()
    my_parser.add_argument('-f', '--file', help="file to read", required=True, type=argparse.FileType('r'))

    my_parser.add_argument('-s', '--start', help="number of lines to read from head of the file", default=3,
                           type=positive_int)
    my_parser.add_argument('-e', '--end', help="number of lines to read from head of the file", default=3,
                           type=positive_int)
    args = my_parser.parse_args()
    print(args)
    with open(args.file.name, args.file.mode) as f:
        lines = f.readlines()
    print(f'First {args.start} from {os.path.basename(args.file.name)}:')
    print(*lines[:args.start], sep='')
    print(f'Last {args.end} from {os.path.basename(args.file.name)}:')
    print(*lines[-args.end:], sep='')


if __name__ == '__main__':
    headtail()

import argparse
import os


def headtail():
    my_parser = argparse.ArgumentParser()
    my_parser.add_argument('-f', '--file', help="file to read", required=True, type=str)

    my_parser.add_argument('-s', '--start', help="number of lines to read from head of the file", default=3,
                           type=int)
    my_parser.add_argument('-e', '--end', help="number of lines to read from head of the file", default=3,
                           type=int)

    args = my_parser.parse_args()
    print(args)
    if args.start < 0 or args.end < 0:
        raise ValueError("values for arguments -s/--start and -e/--end should be positive numbers")
    with open(args.file, 'r') as f:
        lines = f.readlines()
    print(f'First {args.start} from {os.path.basename(args.file)}:')
    print(*lines[:args.start], sep='')
    print(f'Last {args.end} from {os.path.basename(args.file)}:')
    print(*lines[-args.end:], sep='')


if __name__ == '__main__':
    headtail()

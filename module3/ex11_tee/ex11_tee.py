import sys


class Tee(object):
    pass


if __name__ == '__main__':
    f1 = open('tmp/tee1.txt', 'w')
    f2 = open('tmp/tee2.txt', 'w')
    with Tee(sys.stdout, f1, f2) as t:
        t.write('abc\n')
        t.write('def\n')
        t.write('ghi\n')

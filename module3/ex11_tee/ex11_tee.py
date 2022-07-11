import sys


class Tee(object):
    def __init__(self, *fds):
        self.fds = fds

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        for one_file in self.fds:
            one_file.flush()
            one_file.close()

    def write(self, text):
        for one_file in self.fds:
            one_file.write(text)

    def writelines(self, list_text):
        for one_file in self.fds:
            new_list = [line+"\n" for line in list_text[:-1]] + [list_text[-1]]
            one_file.writelines(new_list)


if __name__ == '__main__':
    f1 = open('tee1.txt', 'w')
    f2 = open('tee2.txt', 'w')
    f1.writelines(["sd", "d"])
    with Tee(sys.stdout, f1, f2) as t:
        t.write('abc\n')
        t.write('def\n')
        t.write('ghi\n')
        t.writelines(["text1 ", "text2"])

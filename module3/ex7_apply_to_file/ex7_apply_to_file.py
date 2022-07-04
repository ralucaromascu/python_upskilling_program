import os


def file_length(filename):
    return os.stat(filename).st_size


def filefunc():
    pass


if __name__ == '__main__':
    success_dict, failure_dict = filefunc('/etc/', file_length)
    print(f'Success dict: {success_dict}\nFailure dict: {failure_dict}')

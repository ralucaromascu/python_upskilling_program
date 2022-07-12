import os


def file_length(filename):
    return os.stat(filename).st_size


def filefunc(dir_path, os_command):
    success = {}
    failure = {}
    obj = os.scandir(dir_path)
    for entry in obj:
        if entry.is_file():
            try:
                success[entry.name] = os_command(entry)
            except Exception as e:
                failure[entry.name] = e

    return success, failure


def filefunc_recursively(dir_path, os_command):
    success_rec = {}
    failure_rec = {}
    obj = os.walk(dir_path, topdown=True)
    for root, dirs, files in obj:
        for file in files:
            try:
                success_rec[file] = os_command(os.path.join(root, file))
            except Exception as e:
                failure_rec[file] = e

    return success_rec, failure_rec


if __name__ == '__main__':
    success_dict, failure_dict = filefunc('/etc/', file_length)
    print(f'Success dict: {success_dict}\nFailure dict: {failure_dict}')

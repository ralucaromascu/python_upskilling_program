import os

def get_file_info():
    pass

def get_file_info(pathname):
    for (root, dirs, files) in os.walk(pathname, topdown=True):
        print(root)
        print(dirs)
        print(files)


if __name__ == '__main__':
        get_file_info(os.getcwd())

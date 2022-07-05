class DirFileHash:
    pass


if __name__ == '__main__':
    d = DirFileHash('/etc/')
    print(d['passwd'])

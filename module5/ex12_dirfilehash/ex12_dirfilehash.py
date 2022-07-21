import hashlib
import os


class DirFileHash:
    def __init__(self, dir_name):
        self.dirname = dir_name
        self.files = {}

    def __getitem__(self, filename):
        full_path = os.path.join(self.dirname, filename)
        if os.path.isfile(full_path):
            with open(full_path, 'rb') as f:
                read_content = f.read()
            m = hashlib.md5()
            m.update(read_content)
            hash_value = m.hexdigest()
            return hash_value


if __name__ == '__main__':
    d = DirFileHash('/etc/')
    print(d['passwd'])

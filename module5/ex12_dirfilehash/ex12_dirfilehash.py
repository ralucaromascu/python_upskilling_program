import hashlib
import os


class DirFileHash:
    def __init__(self, dir_name):
        self.dirname = dir_name
        self.files = {}
        if os.path.isdir(dir_name):
            for entry in os.scandir(dir_name):
                if entry.is_file():
                    try:
                        with open(entry, 'rb') as f:
                            read_content = f.read()
                        hash_value = hashlib.md5(read_content).hexdigest()
                        self.files[entry] = hash_value
                    except IOError as e:
                        print(e)

    # def __getitem__(self, item):
    #     if item in self.files:
    #         return self.files[item]
    def __getitem__(self, filename):
        full_path = os.path.join(self.dirname, filename)
        if os.path.isfile(full_path):
            with open(full_path, 'rb') as f:
                read_content = f.read()
            m = hashlib.md5()
            m.update(read_content)
            hash_value = m.hexdigest()
            # self.files[] = hash_value
            return hash_value


if __name__ == '__main__':
    d = DirFileHash('/etc/')
    print(d['passwd'])

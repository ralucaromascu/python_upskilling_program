import hashlib
import os
import time
from pathlib import Path


def get_sha1(pathfile):
    chunk_size = 2048
    md = hashlib.sha1()
    with open(pathfile, 'rb') as f:
        while True:
            chunk = f.read(chunk_size)
            if not chunk:
                break
            md.update(chunk)
        file_hashed_sha1 = md.hexdigest()
    return file_hashed_sha1


class FileList:
    def __init__(self, dir_path):
        self.dir_path = os.path.abspath(dir_path)
        if not Path(self.dir_path).is_dir():
            raise NotADirectoryError
        self.all_file_infos = []
        self.last_timestamp = 0
        self.scan()

    def scan(self):
        self.all_file_infos = []
        for (root, dirs, files) in os.walk(self.dir_path, topdown=True):
            for file in files:
                pathfile = os.path.join(root, file)
                file_info = os.stat(pathfile)
                self.all_file_infos.append(FileInfo(file, file_info.st_mtime, get_sha1(pathfile)))
        self.last_timestamp = time.time()

    def rescan(self):
        update_dict = {'added': [], 'removed': [], 'changed': [], 'unchanged': []}
        new_files_list = []
        for (root, dirs, files) in os.walk(self.dir_path, topdown=True):
            for file in files:
                pathfile = os.path.join(root, file)
                file_info = os.stat(pathfile)
                new_files_list.append(FileInfo(file, file_info.st_mtime, get_sha1(pathfile)))

        update_dict['added'] = [file_obj.filename for file_obj in new_files_list if file_obj not in self.all_file_infos]
        update_dict['removed'] = [file_obj.filename for file_obj in self.all_file_infos if file_obj not in new_files_list]
        for file_obj1 in new_files_list:
            for file_obj2 in self.all_file_infos:
                if file_obj1 == file_obj2:
                    if getattr(file_obj1, 'sha1') != getattr(file_obj2, 'sha1'):
                        update_dict['changed'].append(getattr(file_obj1, 'filename'))
                    else:
                        update_dict['unchanged'].append(getattr(file_obj1, 'filename'))
        self.all_file_infos = new_files_list
        self.last_timestamp = time.time()
        return update_dict


class FileInfo:
    def __init__(self, filename, mtime, sha1):
        self.filename = filename
        self.mtime = mtime
        self.sha1 = sha1

    def __str__(self):
        return f'FileInfo for {self.filename}, mtime {self.mtime}, sha1 {self.sha1}'

    def __eq__(self, other):
        return type(other) == type(self) and self.filename == other.filename


if __name__ == '__main__':
    fd = FileList("../ex25_file_info")
    fd.scan()
    print(str(fd.all_file_infos))
    print(str(fd.last_timestamp))
    with open("new_fileee.txt", 'w') as new_f:
        new_f.write("haha")
    time.sleep(3)
    fd.rescan()
    print(str(fd.last_timestamp))

import hashlib
import os


def get_sha1(pathfile):
    with open(pathfile, 'rb') as f:
        read_content = f.read()
    file_hashed_sha1 = hashlib.sha1(read_content).hexdigest()
    return file_hashed_sha1


class FileList:
    def __init__(self, dir_path):
        self.dir_path = dir_path
        self.all_file_infos = []
        self.last_timestamp = 0

    def scan(self):
        for (root, dirs, files) in os.walk(self.dir_path, topdown=True):
            for file in files:
                pathfile = os.path.join(root, file)
                file_info = os.stat(pathfile)
                self.all_file_infos.append(FileInfo(file, file_info.st_mtime, get_sha1(pathfile)))

    def rescan(self):
        update_dict = {'added': [], 'removed': [], 'changed': []}
        new_files_list = []
        for (root, dirs, files) in os.walk(self.dir_path, topdown=True):
            for file in files:
                pathfile = os.path.join(root, file)
                file_info = os.stat(pathfile)
                new_files_list.append(FileInfo(file, file_info.st_mtime, get_sha1(pathfile)))
        for file_obj in new_files_list:
            if file_obj not in self.all_file_infos:
                update_dict['added'].append(getattr(file_obj, 'filename'))
        for file_obj in self.all_file_infos:
            if file_obj not in new_files_list:
                update_dict['removed'].append(getattr(file_obj, 'filename'))
        for file_obj1 in new_files_list:
            for file_obj2 in self.all_file_infos:
                if file_obj1 == file_obj2 and getattr(file_obj1, 'sha1') != getattr(file_obj2, 'sha1'):
                    update_dict['changed'].append(getattr(file_obj1, 'filename'))
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
    pass

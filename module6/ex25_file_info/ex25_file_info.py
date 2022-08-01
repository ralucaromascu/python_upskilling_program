import hashlib
import os
from datetime import datetime


def get_sha1(pathfile):
    chunk_size = 2048
    md = hashlib.sha1()
    with open(pathfile, 'rb') as f:
        while True:
            chunk = f.read(chunk_size)
            if not chunk:
                break
            md.update(chunk)
        print(md.hexdigest())
        file_hashed_sha1 = md.hexdigest()
    return file_hashed_sha1


def get_file_info(pathname):

    files_dict = []
    for (root, dirs, files) in os.walk(pathname, topdown=True):
        for file in files:
            pathfile = os.path.join(root, file)
            file_info = os.stat(pathfile)
            atime = datetime.fromtimestamp(file_info.st_atime).strftime('%Y-%m-%d %H:%M')
            mtime = datetime.fromtimestamp(file_info.st_mtime).strftime('%Y-%m-%d %H:%M')
            ctime = datetime.fromtimestamp(file_info.st_ctime).strftime('%Y-%m-%d %H:%M')
            files_dict.append({'filename': file,
                               'access_time': atime,
                               'modification_time': mtime,
                               'creation_time': ctime,
                               'sha1': get_sha1(pathfile)})
    return files_dict


if __name__ == '__main__':

    print(get_file_info(os.getcwd()))

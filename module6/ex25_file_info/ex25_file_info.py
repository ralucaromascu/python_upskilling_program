import hashlib
import os
from datetime import datetime
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


def get_file_info(pathname):
    abspath = os.path.abspath(pathname)

    try:
        if not Path(abspath).is_dir():
            raise NotADirectoryError
        files_dict = []
        for (root, dirs, files) in os.walk(abspath, topdown=True):
            for file in files:
                pathfile = os.path.join(root, file)
                file_info = os.stat(pathfile)
                atime = datetime.fromtimestamp(file_info.st_atime).strftime('%Y-%m-%d %H:%M')
                mtime = datetime.fromtimestamp(file_info.st_mtime).strftime('%Y-%m-%d %H:%M')
                ctime = datetime.fromtimestamp(file_info.st_ctime).strftime('%Y-%m-%d %H:%M')
                files_dict.append({'pathfile': pathfile,
                                   'filename': file,
                                   'access_time': atime,
                                   'modification_time': mtime,
                                   'creation_time': ctime,
                                   'sha1': get_sha1(pathfile)})
        return files_dict
    except NotADirectoryError:
        return f"Error: The directory given: [{pathname}] is not a valid one"


if __name__ == '__main__':
    print(get_file_info("Fvds"))
    print(get_file_info("../ex25_file_info"))
    print(get_file_info(os.getcwd()))

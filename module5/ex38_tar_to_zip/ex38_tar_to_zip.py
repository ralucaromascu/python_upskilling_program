import os
import tarfile
import zipfile


class NotTarFile(Exception):
    pass


def create_tarfile(tarfile_name):
    for index, letter in enumerate('abcde', 1):
        with open(os.path.join(os.getcwd(), f'{letter * index}.txt'), 'w') as f:
            f.write(f'{letter * index}\n' * 100)

    tf = os.path.join(os.getcwd(), tarfile_name)
    with tarfile.open(tf, 'w') as t:
        for index, letter in enumerate('abcde', 1):
            t.add(os.path.join(os.getcwd(), f'{letter * index}.txt'))

    return tf


def tar_to_zip(*tar_files, zippath=None):
    if zippath is None:
        zippath = os.getcwd()
    for tar_file in tar_files:
        if not os.path.exists(os.path.join(os.getcwd(), tar_file)):
            raise FileNotFoundError
        if not tarfile.is_tarfile(tar_file):
            raise NotTarFile(f"{tar_file} is not a tar file.")
        prefix = str(tar_file).rsplit('.', 1)[0]
        print(prefix)
        print(tar_file)
        tar = tarfile.open(tar_file)
        tar.extractall(prefix)
        tar.close()

        with zipfile.ZipFile(f'{os.path.join(zippath, prefix)}.zip', 'w') as zipObj:
            for folderName, subfolders, filenames in os.walk(prefix):
                for filename in filenames:
                    file_path = os.path.join(folderName, filename)
                    zipObj.write(file_path)


if __name__ == '__main__':
    # create_tarfile('foo.tar')
    # create_tarfile('bar.tar.gz')
    # create_tarfile('baz.tar.bz2')
    tar_to_zip('foo.tar', 'bar.tar.gz', 'baz.tar.bz2', 'test.txt',
               zippath="/Users/raluca.romascu/python_upskilling_program/module5/ex38_tar_to_zip/test_zippath")

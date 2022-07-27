import os
import tarfile
import zipfile


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
        try:
            tar = tarfile.open(tar_file)
            prefix = str(tar_file).rsplit('.', 1)[0]
            tar.extractall(prefix)
            print(prefix)
            tar.close()
            with zipfile.ZipFile(f'{os.path.join(zippath, prefix)}.zip', 'w') as zipObj:
                for folderName, subfolders, filenames in os.walk(prefix):
                    for filename in filenames:
                        file_path = os.path.join(folderName, filename)
                        zipObj.write(file_path)
        except FileNotFoundError:
            print(f"Error: {tar_file} not found")
        except IsADirectoryError:
            print(f"Error: {tar_file} is not a tar file.")


if __name__ == '__main__':
    # create_tarfile('foo.tar')
    # create_tarfile('bar.tar.gz')
    # create_tarfile('baz.tar.bz2')
    tar_to_zip('foo.tar', 'bar.tar.gz', 'test.txt', 'blabla', 'baz.tar.bz2',
               zippath="/Users/raluca.romascu/python_upskilling_program/module5/ex38_tar_to_zip/test_zippath")

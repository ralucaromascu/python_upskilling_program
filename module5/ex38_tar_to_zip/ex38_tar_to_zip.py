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


def tar_to_zip(*tarfiles, zippath=None):
    if zippath is None:
        zippath = os.getcwd()
    for one_tarfile in tarfiles:
        prefix = str(one_tarfile).split('.tar', 1)[0]
        print(one_tarfile)
        tar = tarfile.open(one_tarfile)
        tar.extractall(prefix)
        tar.close()

        with zipfile.ZipFile(f'{prefix}.zip', 'w') as zipObj:
            for folderName, subfolders, filenames in os.walk(prefix):
                for filename in filenames:
                    file_path = os.path.join(folderName, filename)
                    zipObj.write(file_path)


if __name__ == '__main__':
    # create_tarfile('foo.tar')
    # create_tarfile('bar.tar.gz')
    # create_tarfile('baz.tar.bz2')
    tar_to_zip('foo.tar', 'bar.tar.gz', 'baz.tar.bz2')
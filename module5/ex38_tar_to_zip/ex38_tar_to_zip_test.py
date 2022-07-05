import pytest
import tarfile
import zipfile

from ex38_tar_to_zip import tar_to_zip


@pytest.fixture
def test_tarfile(tmp_path):
    def create_tarfile(tarfile_name):
        for index, letter in enumerate('abcde', 1):
            with open(tmp_path / f'{letter * index}.txt', 'w') as f:
                f.write(f'{letter * index}\n' * 100)

        tf = tmp_path / tarfile_name
        with tarfile.open(tf, 'w') as t:
            for index, letter in enumerate('abcde', 1):
                t.add(tmp_path / f'{letter * index}.txt')

        return tf

    return create_tarfile


def test_tar_to_zip(tmp_path, test_tarfile):
    tar_to_zip(test_tarfile('mytar.tar'), zippath=tmp_path)

    assert len(list(tmp_path.glob('*.zip'))) == 1

    zf = zipfile.ZipFile(tmp_path / 'mytar.zip')
    zf.extractall(path=tmp_path)
    assert len(list(tmp_path.glob('*.txt'))) == 5


def test_multiple_files(tmp_path, test_tarfile):
    tar_to_zip(test_tarfile('mytar1.tar'), test_tarfile('mytar2.tar'), test_tarfile('mytar3.tar'), zippath=tmp_path)
    assert len(list(tmp_path.glob('*.zip'))) == 3

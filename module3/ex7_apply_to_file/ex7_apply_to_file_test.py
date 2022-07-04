import os
from ex7_apply_to_file import filefunc


def file_length(filename):
    return os.stat(filename).st_size


def test_empty_dir(tmp_path):
    d = tmp_path / 'sub'
    d.mkdir()
    s, f = filefunc(d, file_length)
    assert s == {}
    assert f == {}


def test_return_dicts(tmp_path):
    d = tmp_path / 'sub'
    d.mkdir()

    with open(d / 'file1', 'w') as file:
        file.write('abc')

    s, f = filefunc(d, file_length)
    assert type(s) == dict
    assert type(f) == dict


def test_all_success(tmp_path):
    d = tmp_path / 'sub'
    d.mkdir()

    with open(d / 'file1', 'w') as file:
        file.write('abc')
    with open(d / 'file2', 'w') as file:
        file.write('abcdefg')

    s, f = filefunc(d, file_length)
    assert s == {'file1': 3, 'file2': 7}
    assert f == {}


def test_one_fail(tmp_path):
    exc = Exception('Odd file length!')

    def broken_file_length(filename):
        fl = os.stat(filename).st_size
        if fl % 2 == 1:
            raise exc
        return fl

    d = tmp_path / 'sub'
    d.mkdir()

    with open(d / 'file1', 'w') as file:
        file.write('ab')
    with open(d / 'file2', 'w') as file:
        file.write('abcdefg')

    s, f = filefunc(d, broken_file_length)
    assert s == {'file1': 2}
    assert f == {'file2': exc}

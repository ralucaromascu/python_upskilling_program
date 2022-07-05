from ex20_headtail import headtail


def test_no_file(monkeypatch, capsys):
    # TODO: implement
    pass


def test_empty_file(monkeypatch, capsys, tmp_path):
    d = tmp_path / 'sub'
    d.mkdir()
    f = d / 'test-problems.txt'
    # TODO: implement

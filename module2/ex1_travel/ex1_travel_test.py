from io import StringIO
import ex1_travel

empty_place_inputs = StringIO('\n')
one_place_input = StringIO('London, England\n\n')
many_place_inputs = StringIO('''Shanghai, China
Beijing, China
Tel Aviv, Israel
Haifa, Israel
Madrid, Spain
Barcelona, Spain

''')


def test_no_places(monkeypatch):
    ex1_travel.visits.clear()
    monkeypatch.setattr('sys.stdin', empty_place_inputs)
    ex1_travel.collect_places()
    assert len(ex1_travel.visits) == 0


def test_one_place(monkeypatch):
    ex1_travel.visits.clear()
    monkeypatch.setattr('sys.stdin', one_place_input)
    ex1_travel.collect_places()
    assert len(ex1_travel.visits) == 1


def test_many_places(monkeypatch):
    ex1_travel.visits.clear()
    monkeypatch.setattr('sys.stdin', many_place_inputs)
    ex1_travel.collect_places()
    assert len(ex1_travel.visits) == 3


def test_invalid_input(monkeypatch, capsys):
    ex1_travel.visits.clear()
    monkeypatch.setattr('sys.stdin', StringIO('abcd\n\n'))
    ex1_travel.collect_places()
    captured_out, captured_err = capsys.readouterr()
    assert captured_out.strip().startswith("Tell me where you went: That's not a legal city, country combination")
    assert captured_out.strip().endswith("Tell me where you went:")


def test_sorting_cities(monkeypatch, capsys):
    ex1_travel.visits.clear()
    monkeypatch.setattr('sys.stdin', StringIO('Shanghai, China\nBeijing, China\nBeijing, China\n\n'))
    ex1_travel.collect_places()
    captured_out, captured_err = capsys.readouterr()

    ex1_travel.display_places()
    captured_out, captured_err = capsys.readouterr()
    beijing_index = captured_out.index('Beijing')
    shanghai_index = captured_out.index('Shanghai')
    assert beijing_index < shanghai_index


def test_sorting_countries(monkeypatch, capsys):
    ex1_travel.visits.clear()
    monkeypatch.setattr('sys.stdin', StringIO('Haifa, Israel\nLondon, England\nNew York, USA\n\n'))
    ex1_travel.collect_places()
    captured_out, captured_err = capsys.readouterr()

    ex1_travel.display_places()
    captured_out, captured_err = capsys.readouterr()
    israel_index = captured_out.index('Israel')
    england_index = captured_out.index('England')
    usa_index = captured_out.index('USA')
    assert england_index < israel_index
    assert israel_index < usa_index


def test_counting(monkeypatch, capsys):
    ex1_travel.visits.clear()
    monkeypatch.setattr('sys.stdin', StringIO('Shanghai, China\nBeijing, China\nBeijing, China\n\n'))
    ex1_travel.collect_places()
    captured_out, captured_err = capsys.readouterr()
    assert len(ex1_travel.visits['China']) == 2

    ex1_travel.display_places()
    captured_out, captured_err = capsys.readouterr()
    assert 'Beijing (2)' in captured_out
    assert 'Shanghai' in captured_out

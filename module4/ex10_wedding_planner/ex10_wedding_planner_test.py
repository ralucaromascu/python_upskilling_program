import pytest
from ex10_wedding_planner import GuestList, Person, TableFull


@pytest.fixture
def some_people():
    return [Person('Waylon', 'Dalton'),
            Person('Justine', 'Henderson'),
            Person('Abdullah', 'Lang'),
            Person('Marcus', 'Cruz'),
            Person('Thalia', 'Cobb'),
            Person('Mathias', 'Little'),
            Person('Eddie', 'Randolph'),
            Person('Angela', 'Walker'),
            Person('Lia', 'Shelton'),
            Person('Hadassah', 'Hartman'),
            Person('Joanna', 'Shaffer'),
            Person('Jonathon', 'Sheppard')]


@pytest.fixture
def populated_tables(some_people):
    gl = GuestList()
    for table_number, one_person in enumerate(some_people):
        gl.assign(one_person, table_number+1)
    return gl


def test_empty_table():
    gl = GuestList()
    assert len(gl) == 0
    assert gl.free_space() == {}


def test_with_a_few_people(some_people):
    gl = GuestList()
    for table_number, one_person in enumerate(some_people[:5]):
        if table_number == 0:
            gl.assign(one_person, None)
        else:
            gl.assign(one_person, table_number)
    assert len(gl) == 5
    assert len(gl.unassigned()) == 1
    assert gl.unassigned() == [some_people[0]]
    for table_number in range(1, 5):
        assert gl.table(table_number) == [some_people[table_number]]


def test_get_guests(some_people, populated_tables):
    gl = populated_tables
    assert gl.guests() == some_people


def test_sorted_guests(some_people):
    gl = GuestList()
    for one_person in some_people[:5]:
        gl.assign(one_person, 1)
    assert gl.guests()[0].first == 'Thalia'
    assert gl.guests()[4].first == 'Abdullah'


def test_table_full(some_people):
    gl = GuestList()
    for one_person in some_people[:GuestList.max_at_table]:
        gl.assign(one_person, 1)
    assert len(gl) == GuestList.max_at_table
    with pytest.raises(TableFull):
        gl.assign(some_people[GuestList.max_at_table], 1)


def test_table_free_space(some_people):
    gl = GuestList()
    for one_person in some_people[:GuestList.max_at_table - 1]:
        gl.assign(one_person, 1)
    assert (gl.free_space()) == {1: 1}
    one_person = some_people[1]
    gl.assign(one_person, 2)
    assert (gl.free_space()) == {1: 2, 2: GuestList.max_at_table - 1}


def test_repr(some_people):
    gl = GuestList()
    assigned_people = some_people[:GuestList.max_at_table]
    for one_person in assigned_people:
        gl.assign(one_person, 1)

    output = str(gl)
    assert output.startswith('1\n')
    for one_person in assigned_people:
        assert f'{one_person.last}, {one_person.first}' in output

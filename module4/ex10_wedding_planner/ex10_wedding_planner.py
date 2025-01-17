from collections import namedtuple
from operator import attrgetter

Person = namedtuple('Person', ['first', 'last'])


class TableFull(Exception):
    pass


class GuestList:
    max_at_table = 10

    def __init__(self):
        self.persons = {}
        self.tables = {}

    def __len__(self):
        return len(self.persons)

    def _add_to_table(self, person, table_number):
        if table_number is not None:
            if table_number in self.tables:
                self.tables[table_number].append(person)
                # if len(self.tables[table_number]) > self.max_at_table:
                #     raise TableFull("Table is already full")
            else:
                self.tables[table_number] = [person]
        else:
            if 'unassigned' in self.tables:
                self.tables['unassigned'].append(person)
            else:
                self.tables['unassigned'] = [person]

    def assign(self, person, table_number):
        if table_number is not None and table_number in self.tables:
            if len(self.tables[table_number]) >= self.max_at_table:
                raise TableFull("Table is already full")
        if person in self.persons:
            self.tables[self.persons.get(person)].remove(person)
            self._add_to_table(person, table_number)
        else:

            self.persons[person] = table_number
            self._add_to_table(person, table_number)

    def table(self, table_number):
        return self.tables[table_number]

    def unassigned(self):
        return self.tables['unassigned']

    def free_space(self):
        return {key: self.max_at_table - len(self.tables[key]) for key in self.tables}

    def guests(self):
        dict_tables = {key: sorted(self.tables[key], key=attrgetter('last', 'first'))
                       for key in self.tables if type(key) == int}
        return [item for persons in [dict_tables[key] for key in sorted(dict_tables.keys())] for item in persons]

    def __str__(self):
        text = ""
        dict_tables = {key: sorted(self.tables[key], key=lambda elem: (elem.last, elem.first))
                       for key in self.tables if key != 'unassigned'}
        for key in sorted(dict_tables.keys()):
            text = text + f"{key}\n"
            for person in dict_tables[key]:
                text = text + f"\t{person.last}, {person.first}\n"
        return text


if __name__ == '__main__':
    gl = GuestList()
    gl.assign(Person('Waylon', 'Dalton'), 1)
    gl.assign(Person('Justine', 'Henderson'), 1)
    gl.assign(Person('Abdullah', 'Lang'), 3)
    gl.assign(Person('Marcus', 'Cruz'), 1)
    gl.assign(Person('Thalia', 'Cobb'), 2)
    gl.assign(Person('Mathias', 'Little'), 2)
    gl.assign(Person('Eddie', 'Randolph'), None)
    gl.assign(Person('Angela', 'Walker'), 2)
    gl.assign(Person('Lia', 'Shelton'), 3)
    gl.assign(Person('Hadassah', 'Hartman'), None)
    gl.assign(Person('Joanna', 'Shaffer'), 3)
    gl.assign(Person('Jonathon', 'Sheppard'), 2)

    print(len(gl))
    print(gl.table(2))
    print(gl.unassigned())
    pers = Person('Joanna', 'Shaffer')
    gl.assign(pers, 3)
    print(gl.free_space())
    print(gl.guests())
    print(gl)


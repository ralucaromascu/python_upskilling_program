# Wedding planner

Hooray! It's time for a wedding!

Fine, so it's only a virtual wedding. But we have a bunch of guests, and we need to organize them in some way. We're going to do that with a `GuestList` class. We'll create an instance of this class, and add our guests (as named tuples) into the guest list, along with a table number. We'll then be able to ask our class for a complete guest list by table, as well as a report of which tables aren't yet full.

Here's how the class should work:

```python
# Person should be a named tuple, with "first" and "last" attributes
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
```

In the above code, I've created a guest list. Each `Person` is then created and assigned to a table. If we assign a person to table `None`, they aren't assigned.

We will assume, for the purposes of this exercise, that everyone in the world has a unique name.

We will also assume that a maximum of 10 people can be added to a given table. Attempting to add more than 10 people to a table results in a `TableFull` exception.

Now we want to run a few reports on our guest list:

1. How many guests are there, total? We should be able to run the following to get an integer back:

```python
len(gl)
```

2. What guests are at a given table? We should be able to run the following and get a list of Person objects back:

```python
gl.table(2)
```

3. What guests aren't assigned to any table? We should be able to run the following and get a list of Person objects back:
```python
gl.unassigned()
```

4. Given a Person object, we should be able to assign them to a table:
```python
p = Person('Joanna', 'Shaffer')
gl.assign(p, 3)
```
If the person is already in the system, but is assigned to another table (or to no table at all), then they will now be assigned to a new table.

If the person isn't already in the system, then they will be added and then assigned to a table.

If there is no room at the table (i.e., there are already 10 guests there), then we should raise a `TableFull` exception.

5. We should also be able to learn how much space is available at each table. The following should return a dictionary of table names (keys) and remaining space (values) for each table:
```python
gl.free_space()
```

6. We should be able to get a list of all guests, sorted first by table number, then by last name, and finally by first name:
```python
gl.guests()
```

7. Finally, we should be able to get the above list printed nicely:
```python
print(gl)
```

I'm thinking something like:

```
2
    last, first
    last, first
3
    last, first
    last, first
4
    last, first
    last, first
    last, first
```
    
Who said weddings are easy?

The code needs to pass the tests in [ex10_wedding_planner_test.py](ex10_wedding_planner_test.py) file.

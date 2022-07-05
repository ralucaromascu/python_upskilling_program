# better_repr

We previously used a decorator to modify a function — specifically, how often a function could be run. This week, we'll start a two-part exercise to use decorators in a different way, to modify the way in which a class is defined and used.

Something that has always bothered me in Python is the default output from the `__repr__` and `__str__` methods. Is there anyone who believes that if I define a class in the following way:
   
```python
class Bar(object):
    pass
```

That the most reasonable output from:

```python
b = Bar()
print(b)
```

Will be:
```
<__main__.Bar at 0x1043991d0>
```
No, I didn't think so. This is pretty useless. I don't need to know the address of the object in memory, and I certainly would like to know a bit more than the class. For example, I'm generally curious to see the object's attributes.

Well, the time has come to change this. This week, we're going to create a decorator that, when applied to a class, lets us have an alternative output to the defaults. For example:

```python
@betterrepr
class Foo(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

f = Foo(10, [1, 2, 3, 4, 5])
print(f)
```

I want my `betterrepr` decorator to modify `__repr__` such that the output from the above code will be:

```
Instance of Foo, vars = {'x': 10, 'y': [1, 2, 3, 4, 5]}
```

The code needs to pass the tests in [ex30_better_repr_test.py](ex30_better_repr_test.py) file.

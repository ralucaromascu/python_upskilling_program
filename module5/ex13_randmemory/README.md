# RandMemory

We want to generate random numbers, but also remember (and be able to access) the history of numbers we've generated. For this, we'll create a class `RandMemory` with a property `get` that returns a random number:

```python
r = RandMemory(1,100)   # produces integers between 1 and 100
r.get                   # returns a number
r.get                   # returns a number
r.get                   # returns a number
r.history()             # returns a list of numbers previously generated
```

Note that `r.get` is **not** invoked as a method! However, it does invoke code.

**Hint:** This means creating a "property", which looks to the outside as if it's a data attribute, but from the inside works as a method. You don't need to create a `setter` property for this attribute.

The code needs to pass the tests in [ex13_randmemory_test.py](ex13_randmemory_test.py) file.

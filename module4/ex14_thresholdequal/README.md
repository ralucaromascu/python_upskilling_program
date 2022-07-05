# ThresholdEqual

This week, we're going to write a simple class that lets us pretend that things are equal, even when they are not.

I want you to create a `ThresholdEqual` class. Each instance of this class will have a single attribute, `x`, which we will assume is always numeric (you can check that it's numeric at creation time if you want, but you don't have to).

Normally, if we compare two numeric values with `==`, the answer is cut and dried: either they're the same, or not.

But with `ThresholdEqual`, they can be equal even if they're not equal. That is, there will be a class attribute `threshold` that will determine the tolerance. If the tolerance is set to `2`, then we should see the following:

```python
te1 = ThresholdEqual(10)
te2 = ThresholdEqual(6)

print(te1 == te2)        # prints "False"

te1 = ThresholdEqual(10)
te2 = ThresholdEqual(9)

print(te1 == te2)        # prints "True"
```

In other words, these two objects will be considered equal if their `x` attributes are within 2 of one another, and not equal otherwise.

As it stands, this class is pretty useless, and is meant for teaching purposes. However, you should feel free to add functionality that will allow all of our favorite operators and methods to work on instances of `ThresholdEqual`, as well.

If you want to go even further than that, then you can have `__init__` take an optional parameter indicating the tolerance for that particular instance, rather than for the entire class. However, you'll then need to think about what happens if you compare two instances with different tolerances.

The code needs to pass the tests in [ex14_thresholdequal_test.py](ex14_thresholdequal_test.py) file.

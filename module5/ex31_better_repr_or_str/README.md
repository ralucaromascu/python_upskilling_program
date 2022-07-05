# Better repr or str

Last week, we created a decorator that overrode the builtin `__repr__` method, replacing it with a hardcoded solution defined by the decorator. This week, we'll improve this decorator to give it a bit more flexibility, letting the user replace `__repr__` and/or `__str__` with either externally defined functions or (by default) internally defined ones.

The decorator will take two optional arguments, called `newstr` and `newrepr`. It is expected that the passed values will be functions that will replace the default `__repr__` and `__str__` methods. If `newstr` isn't defined, then nothing special will happen. But if `newrepr` isn't passed, then we'll use the same default value as last time, overriding object's `__repr__`.

The code needs to pass the tests in [ex31_better_repr_or_str_test.py](ex31_better_repr_or_str_test.py) file.

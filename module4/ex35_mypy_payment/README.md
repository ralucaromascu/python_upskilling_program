# MyPy Payment

Last week, we explored how we can use an abstract base class to create and enforce an API for subclasses.

The thing is, there are numerous ways in which we can define and enforce APIs. The traditional way to do this in the Python world has been documentation: you document your functions, classes, and modules using docstrings, and the users are responsible for reading that documentation and putting it into practice.

As the number and size of companies using Python has grown, companies and groups have needed more ways to ensure that people are calling functions and methods with the right parameters.

But how can we do that? After all, Python is a dynamic language. So there's no compiler that checks types. And besides, what types would it check? And how can you add that sort of type checking to a dynamic language?

Over the last few years, the MyPy project has been working on solving precisely this problem. MyPy doesn't change Python; rather, it takes advantage of Python 3's type annotations, and is a precompiler that double-checks you're calling functions and methods with the right types of arguments — and that the return type is doing the right thing, too.

When you use MyPy on the methods of an abstract base class, you can enforce the parameter and return types on subclass methods.

This week's exercise is to take last week's `AbstractPayment` class, and to use MyPy to annotate its methods such that a subclass will not only have to implement the abstract methods, but will take the right types of parameters, and will also enforce the right return types.

Specifically:
- in all the methods, `user_id`, `amount`, and `merchant_id` should all be integers, but `currency` should be a string
- the return value from authorize_payment should be `True` or `False`
- the return value from `charge_payment` and `reverse_payment` should be an integer

MyPy takes a bit of time to get used to, but once you get into the rhythm of things, it can really help you to ensure that your code is running smoothly. Note that there are pseudo-types that can help you to describe functions that take different types of arguments (e.g., sequences) or that return different types (e.g., an integer or None). We're not going to get that fancy here; the key thing is to understand MyPy enough that you can annotate the abstract class, and thus enforce an API — not just a method's existence, but also its signature.

[Here](http://mypy.readthedocs.io/en/latest/cheat_sheet_py3.html) is a great summary of MyPy functionality for Python 3.

The [tests](ex35_mypy_payment_test.py) for this week are roughly the same as they were last week. However, that's because the real "test" this week is not whether the code will run, but whether (and how much) we can turn the screws on our classes, such that MyPy will both test things and fail to complain.

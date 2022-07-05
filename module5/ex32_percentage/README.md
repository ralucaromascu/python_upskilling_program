# Percentage

This week, we're going to explore the world of descriptors. If you know what properties are (and we covered them in a previous exercise, so I hope that you do!), then you can think of descriptors are generalized properties. That is, if you have a property that you'll want to use in more than one class, then it is probably better to implement it as a descriptor.

The descriptor we want to create will allow classes to store integer percentages. This means that any integer from 0 to 100 (inclusive) will be a legal value for this descriptor. Non-integers and numbers higher than 100 or lower than 0 should result in an exception being thrown, indicating that the type and/or value is wrong..

In other words, given this descriptor, I should be able to create a class like this:

```python
class Foo(object):
    participation = Percentage()

f = Foo()
f.participation = 500       # results in a PercentageTooHighError
f.participation = -5        # results in a PercentageTooLowError
f.participation = 'a'       # results in a PercentageNotANumber
f.participation = 50.3
f.participation             # returns 50, the result of truncating to get an int
```

The descriptor should ensure that different instances contain their separate values. I should thus be able to say:

```python
f1 = Foo()
f1.participation = 30

f2 = Foo()
f2.participation = 70

print(f1.participation)     # prints 30, not 70
```

The code needs to pass the tests in [ex32_percentage_test.py](ex32_percentage_test.py) file.

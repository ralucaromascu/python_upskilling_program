# Abstract payment

This week, we'll explore the idea of an abstract base class, and how to work with it in Python.

We've already seen, and experimented with, classes and subclasses. An abstract base class is a class that is designed not to have any instances. Rather, it's designed to be subclassed. Moreover, it can force its subclasses to implement one or more methods, thus enforcing an API.

I personally have mixed feelings about how much abstract base classes should be used. But some people really like them: they basically allow you to define an interface or protocol in Python using code, rather than documentation.

For this week's exercise, we're going to assume that we're creating a payment system. We want to allow any payment method to connect to our system, using (of course) a Python class. That is, there will be one Python class for credit cards, another for PayPal, another for Bitcoin, etc.

What I want is for you to create an `AbstractPayment` class. Again, the idea is that no one will actually create an instance of `AbstractPayment`. Rather, you should then be able to subclass it.

Every subclass must implement the following methods:

```python
authorize_payment(user_id, amount, currency)            # returns True or False
charge_payment(user_id, amount, currency, merchant_id)  # returns a transaction ID number or raises CannotCharge
reverse_payment(user_id, amount, currency, merchant_id) # returns a transaction ID number or raises CannotReverse
```

You don't really need to go deep into these methods. And of course, you can create additional methods. But the idea is that if you try to do this:

```python
class MyNewPayment(AbstractPayment):
    pass

mnp = MyNewPayment()
```

We'll be prevented from doing so, thanks to the abstract class definition.

FYI, you'll want to use the [`abc` module](https://docs.python.org/3/library/abc.html) in Python's standard library to create an abstract base class.

The code needs to pass the tests in [ex34_abstract_payment_test.py](ex34_abstract_payment_test.py) file.

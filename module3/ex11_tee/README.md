# tee

Here's an exercise based on a question that I recently got from a student in class: the Unix `tee` command lets you write data not only to standard output, but also to a file. This is useful if you want to see the result of a command on the screen, but also write that output to a file.

This week, we'll make it possible to create our own tee-like system in Python. The basic idea is that you'll create an instance of the `Tee` class, passing it all the file-like objects that you want. For example:

```python
import sys

f1 = open('/tmp/tee1.txt', 'w')
f2 = open('/tmp/tee2.txt', 'w')
t = Tee(sys.stdout, f1, f2)
```

Now, when I invoke `t.write` or `t.writelines`, the method call will be applied to each of these file-like objects. If an error occurs, then the exception will be raised as usual:

```python
t.write('abc\n')
t.write('def\n')
t.write('ghi\n')
```

Invoking the above, assuming that there are no exceptions, will print the three strings on the screen, as well as to the two other files.

For additional credit, make our `Tee` class a context manager, meaning that we can use it within a `with` statement to guarantee that all the file-like objects are flushed and closed.

```python
f1 = open('tmp/tee1.txt', 'w')
f2 = open('tmp/tee2.txt', 'w')
with Tee(sys.stdout, f1, f2) as t:
    t.write('abc\n')
    t.write('def\n')
    t.write('ghi\n')
```

The code needs to pass the tests in [ex11_tee_test.py](ex11_tee_test.py) file.

# All word count

This week, we'll experiment with threads. Here's the basic idea: I want to count all of the words in all of the files that match a particular pattern (we'll use `glob.glob` to retrieve the files matching that pattern).

The idea is that I can invoke the function

```python
count_words('/foo/bar/*.txt')
```

and all of the words (i.e., strings separated by one or more whitespace characters) will be counted.

I want you to implement this twice:
1. `count_words` goes through each of the matching files sequentially
2. `count_words` opens a thread for each of the files

In order to implement the second version of `count_words`, you might need to learn a bit about how threading works in Python. In particular, you'll want to use the `threading` library (and the `Thread` class within it), including the `start` and `join` methods. You'll also probably want to use a `Queue` (in the `queue` module) to synchronize the information you've found so far.

The code needs to pass the tests in [ex18_all_word_count_test.py](ex18_all_word_count_test.py) file.

# Apply to file

This week, we'll write a function that takes a function as an argument. Actually, the function takes two arguments:
- a directory name (string)
- a function

The function will be applied to each file in the directory.

The output from the function's execution on each file will be returned as part of a dictionary, in which the filenames are the keys and the results are the values.

For example, if we call

```python
import os

def file_length(filename):
    return os.stat(filename).st_size

success_dict, failure_dict = filefunc('/etc/', file_length)
```

The result will be two dictionaries:
- the first dictionary's keys are the filenames and the output from running the function, when no exception was raised
- the second dictionary's keys are the filenames and the exception object when one was raised.

So, in the call above, if no exceptions were raised, then the first dictionary returned would consist of the filenames in `/etc/`, with the length of each file as a value. The second dictionary would be empty.

The code needs to pass the tests in [ex7_apply_to_file_test.py](ex7_apply_to_file_test.py) file.

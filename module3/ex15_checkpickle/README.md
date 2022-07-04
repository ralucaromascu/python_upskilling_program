# Checkpickle

This week, we're going to explore Python's `pickle` module. In other languages, we talk about "serialization" or "marshaling" of objects — but in Python, we are more whimsical, and use "pickle."

We're going to experiment with pickling in the context of a function `checkpickle` that when run lets you add to, review, and restore the contents of an address book. The address book itself will contain three fields: first name, last name, and email.

When the function is invoked, it asks the user to enter a command. Avaialble commands are:
- `q`: Quit from the program (function)
- `l`: List all people in the address book in format `{last_name}, {first_name}: email {email}`
- `a`: Add a new person to the address book
- `r`: Restore the address book to the stage from a specific timestamp

The `q` and `l` commands are, I think, pretty much self-explanatory.

The `a` command is mostly self-explanatory. People will be prompted to enter three different pieces of information (first name, last name, and e-mail address). Doing so will create a new record in the database (I use a list of dicts, with each dict containing keys `first_name`, `last_name`, and `email`.) Don't worry about the uniqueness of people in the system, or of many other things you'll have to consider in writing a real address-book program.

The key thing about `a` is that after adding a new person (dict) to the list, it'll also checkpoint (i.e., write to disk) the current value of `people` to a file using `pickle`. This means that if I add five people to the address book, there will be five different checkpoint files. Each file will consist of a common "stem" filename, followed by a timestamp.

The `r` command will allow users to restore the database to any point: when a user enters a `r`, they are prompted to enter a timestamp. If a checkpoint file exists at that timestamp, the current value of the `people` list will be replaced with the value from disk.

The function takes one optional argument, the stem (i.e., pathname and start of the filename) used for storing and retrieving the pickled data.

As a result, the first line of my function definition looks like:

```python
def checkpickle(cp_stem='people-checkpoint-'):
```

The code needs to pass the tests in [ex15_checkpickle_test.py](ex15_checkpickle_test.py) file.

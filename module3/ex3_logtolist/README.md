# logtolist

This week, we're going to play with files. Specifically, logfiles.

A lot of the Python developers I teach (and work with) work with logfiles of various sorts, and want to work with those files in various ways. This week, we'll see how we can turn the logfile into a list of dictionaries, making it easier to manipulate.

For the purposes of this exercise, we'll be looking at this access log file: [mini-access-log.txt](mini-access-log.txt)

Each line of this logfile looks like the following:

```
67.218.116.165 - - [30/Jan/2010:00:03:18 +0200] "GET /robots.txt HTTP/1.0" 200 99 "-" "Mozilla/5.0 (Twiceler-0.9 http://www.cuil.com/twiceler/robot.html)"
```

As you can see:
- the fields aren't separated by whitespace, but are still recognizable to a human
- each line starts with an IP address
- between square brackets, we have the timestamp — date, time, and then the timezone
- following the timestamp, inside of double quotes `"`, we have the HTTP request (you can assume that in this file, all the request start with the word GET)
- there are other fields as well, but these are the ones that interest me

The exercise is to write a function that, when given a filename, returns a list of dictionaries. Each dict should have the following keys:
- `ip_address`, containing the IP address
- `timestamp`, containing the timestamp (not including the square brackets, but everything inside them)
- `request`, containing the HTTP request (not including the double quotes, but everything inside them)

Thus, the above line from mini-access-log.txt would look like this:

```python
{
    'ip_address': '67.218.116.165',
    'timestamp': '30/Jan/2010:00:03:18 +0200',
    'request': 'GET /robots.txt HTTP/1.0',
}
```

We'll transform the file into a list of dicts, each of which looks that. There are 206 lines in the file, which means that this list will contain 206 dictionaries, each with these three key-value pairs.

Using a regular expression will definitely help here — but if you don't know regexps, then don't worry, you can still get it to work. That said, it'll be a bit clunky.

The code needs to pass the tests in [ex3_logtolist_test.py](ex3_logtolist_test.py) file.

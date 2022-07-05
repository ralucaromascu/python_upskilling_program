# tar to zip

If you're a Unix user, then you're probably used to working with tar files.

Some background: Way back when, if you wanted to take a bunch of files and combine them into a single file, you would use the `ar` command (yes, `ar` still exists on Unix systems, including the Mac OS). If you wanted to store the archive onto tape, you would use the `tape archive` command, or `tar`. Over time, the `tar` command became a standard way to take multiple files and combine them into a single one. For example, if I want to share a number of PDF files with a friend, I would first create a tar file, and then send a single file.

One thing that `tar` didn't do was to compress the resulting archive file. A number of different compression systems were thus born. One was called `compress` (again, it still exists), and it not only compressed a file, but added the "Z" suffix. The GNU project, the source of many free and open-source programs, eventually created their own compression system, which they called `gzip`, and which gave files a "gz" suffix. More recently, there's a `bzip2` program that uses a "bz2" suffix when compressing.

The combination of `tar` + a compression program has thus been standard in the Unix world for many years. And while `tar` and the various compression systems all exist under Windows, they're far less common. Instead, Windows people use zip files, created and extracted using many different versions of the `zip` program. The story of Phil Katz's PKZIP for Windows is a fascinating soap opera unto itself. If you weren't there at the time, I recommend reading [this](http://www.bbsdocumentary.com/library/CONTROVERSY/LAWSUITS/SEA/pkzip.htm).

Nowadays, it's safe to say that most Unix people are able to work with zip files. There are a number of implementations, and while `unzip` isn't installed by default with many Linux distributions, it's not a problem to add it. However, the reverse cannot be said for Windows users. When they see a file with a "tar.gz" suffix, they are (in my experience) completely unsure of what to do with it.

This week, we'll write a function that takes one or more filenames, each of which is assumed to be a tarfile (with or without compression). For each filename, the function will create a new zipfile with the same contents, but (obviously) in ".zip" format rather than in ".tar.gz" format.

Python comes with two modules, `zipfile` and `tarfile`, that should help you with that. Note that the `tarfile` module knows how to deal with various types of compression automatically, which is pretty impressive and amazing.

For example, if I write:

```python
tar_to_zip('foo.tar', 'bar.tar.gz', 'baz.tar.bz2')
```

I'm going to expect that in the current directory, we'll then have three files: `foo.zip`, `bar.zip`, and `baz.zip`, each of which will contain the same contents as the respective tarfiles, but in zip format, instead.

If you get a file that cannot be "untared" for whatever reason, then print an error or warning message, but continue.

You can also pass a value to the `zippath` parameter, indicating where you want the zipfile to be created.

I'll assume for the purposes of this exercise that it's OK to untar the contents of the tarfile in the current directory, although if you can do it in a temporary directory (e.g., '/tmp/'), all the better.

The code needs to pass the tests in [ex38_tar_to_zip_test.py](ex38_tar_to_zip_test.py) file.

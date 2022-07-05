# Solution

This week, we're exploring a few things that often come together:

1. Downloading information from the Internet
2. Processing a dictionary file
3. Using sets and comprehensions
4. Some additional work with sets

If you haven't worked with sets before, then I highly recommend you try including them in your work. I'm not going to claim that you'll use them each and every day, but there are certain tasks that sets make oh-so-much easier and better.

First and foremost, let's talk about how to download things from the Internet. Specifically, I wanted you to be able to download an HTML file from the Web, and remove the HTML tags. This requires two different packages, both of which are available and popular on PyPI: `requests`, which lets you retrieve things via HTTP, and `BeautifulSoup`, which parses HTML and lets you play with it.

What we're interested in doing is downloading the content from one or more URLs, and then grabbing the text from there. The problem is that JavaScript and CSS are often seen as "text", albeit within the `script` and `style` tags. That's why we need to just get rid of those tags altogether, so that we don't have to worry about mixing their content in with our "real" textual content.

The way to do this is in a multi-step process:
- download the content
- parse it with Beautiful Soup
- remove the `script` and `style` tags
- get the text (we can do that with the following code):

```python
for one_url in urls:
    body = requests.get(one_url).content

    soup = BeautifulSoup(body, 'lxml')
    for script in soup(["script", "style"]):
        script.extract()        

    text = soup.get_text()
```

Notice that I'm iterating over a list of URLs `urls` here, which is part of the overall solution that lets me check a bunch of places at once. `requests` has a great `get` method, whose response then has a `content` attribute that returns the contents.

The `BeautifulSoup` parser automatically uses the `lxml` parser in order to look through the HTML/XML downloaded content, but if you don't specify it explicitly, then you get a nasty warning message. So I decided to make it explicit. I followed the directions in the Beautiful Soup documentation to remove those `script` and `style` tags.

Finally, I used the `BeautifulSoup` `get_text` method to retrieve the text from within the tags. And sure enough, I then had text!

The next thing I wanted to do was find out which words in the document didn't appear in the dictionary. I find that using sets for this sort of tasks is extremely useful. Sets have a great `-` (subtraction) implementation, letting me subtract one set from another. In order for this to work, though, I needed to have a dictionary as a set. Luckily, most Unix systems have them. I used a set comprehension to create a set of the dictionary:

```python
dict_filename = '/usr/share/dict/words'

dict_words = {one_word.strip() for one_word in open(dict_filename)}
```

I then turned the current URL's content into a list of words, which I turned into a set. And then I simply calculated (using `len`) how many words from the article weren't in the dictionary. Finally, I used two dicts to keep track of the score for each URL:

```python
not_in_dict = {}
words = text.split()
not_in_dict[one_url] = len(set(words) - dict_words)
```

Next, I wanted to know the average length of words in the article. For this, I used a list comprehension, turning each word into its length. That allowed me to then calculate the average word length:

```python
average_length = {}
average_length[one_url] = sum([len(one_word) for one_word in words]) / len(words)
```

Once I was done going through the URLs, I could then print a report describing each of the calculations:

```python
for one_url in urls:
    print(f'{one_url:20}: {average_length[one_url]} {not_in_dict[one_url]}')
```

And there we have it!

I'd like you to make a jot.py program that will allow us "jot down" quick thoughts to look at later.

This program should save ideas along with the current date in a ~/jot.txt file (meaning a jot.txt in the current user's home directory).

When you run jot.py, it should prompt you to enter a one-line thought:
~~~
$ python3 jot.py
jot: ▮
~~~
That ▮ symbol above is where we would start typing.

Let's say we run jot.py, type raisin M&M and then we hit Enter:

~~~
$ python3 jot.py
jot: raisin M&M
~~~
Now, we made that note on January 1st 2023, if we look in the jot.txt file in our home directory (/home/trey in my case) we'll see:

~~~
2023-01-01 raisin M&M
~~~
If we run jot.py again and type in another idea later that day:

~~~
$ python3 jot.py
jot: type hint search engine
~~~
We'll see two lines in our ~/jot.txt file:
~~~
2023-01-01 raisin M&M
2023-01-01 type hint search engine
~~~
If two days later, we write down another idea:
~~~
$ python3 jot.py
jot: socks, but for tacos
~~~
Then we'll see three lines in our ~/jot.txt file:
~~~
2023-01-01 raisin M&M
2023-01-01 type hint search engine
2023-01-03 socks, but for tacos
~~~
#### Write a function format_time that accepts an integer on seconds and returns a timestamp string.

~~~format_time(333)
'5:33'
~~~
The timestamp string should be in the format M:SS where M represents the minutes and SS represents the remaining seconds.
~~~
format_time(119)
'1:59'
format_time(3715)
'61:55'
format_time(3600)
'60:00'
~~~
Note that the seconds should always be represented by 2 digits, but the minutes may be represented by just 1 digit:
~~~
format_time(301)
'5:01'
format_time(0)
'0:00'
format_time(90061)
'1501:01'
format_time(61)
'1:01'
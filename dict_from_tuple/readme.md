### Write a dict_from_tuple function which accepts a list of tuples of any length and returns a dictionary which uses the first item of each tuple as keys and all subsequent items as values.

~~~
dict_from_tuple([(1, 2, 3, 4), (5, 6, 7, 8)])
{1: (2, 3, 4), 5: (6, 7, 8)}
dict_from_tuple([(1, 2, 3), (4, 5, 6), (7, 8, 9)])
{1: (2, 3), 4: (5, 6), 7: (8, 9)}
~~~
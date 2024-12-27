### Write a function len_or_none that returns the length of a given object or None if the object has no length.

Strings have a length:
~~~
len_or_none("hello")
5
~~~
But numbers don't:
~~~
len_or_none(4)
print(len_or_none(4))
None
~~~
Lists and range objects have a length:
~~~
len_or_none([])
0
len_or_none(range(10))
10
~~~
But zip objects don't:
~~~
len_or_none(zip([1, 2], [3, 4]))
print(len_or_none(zip([1, 2], [3, 4])))
None
~~~
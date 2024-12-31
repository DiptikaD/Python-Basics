### Write a function flip_dict, that takes a dictionary as input and returns a new dictionary with the dictionary keys and values flipped.
~~~
flip_dict({"Python": "2015-09-15", "Java": "2015-09-14", "C": "2015-09-13"})
{'2015-09-15': 'Python', '2015-09-14': 'Java', '2015-09-13': 'C'}
~~~
If your dictionary contains repeated values, the last key for that value should "win":
~~~
flip_dict({"Python": "2015-09-15", "Java": "2015-09-14", "C": "2015-09-15"})
{'2015-09-15': 'C', '2015-09-14': 'Java'}
~~~
You likely won't need to do anything special to meet that second requirement.

You can assume all values in the given dictionary will be strings, numbers, or other hashable objects.

### Bonus 1
For the first bonus, I'd like you to accept an optional error_on_duplicates argument which, when True, will cause flip_dict to raise a ValueError exception if the given dictionary has repeated values.
~~~
pairs = {"Garnet": "Amethyst", "Steven": "Rose", "Pearl": "Rose"}
flip_dict(pairs, error_on_duplicates=True)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 3, in flip_dict
ValueError: Dictionary has duplicate values
~~~
Note that if error_on_duplicates isn't specified, the last key for each value should still "win", just as before:
~~~
flip_dict(pairs)
{'Amethyst': 'Garnet', 'Rose': 'Pearl'}
~~~
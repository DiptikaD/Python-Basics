### Problem Statement
#### Make a function split_in_half that splits a list in half and returns both halves.
~~~
split_in_half([1, 2, 3, 4])
([1, 2], [3, 4])
split_in_half([1, 2, 3, 4, 5])
([1, 2], [3, 4, 5])
split_in_half([1, 2])
([1], [2])
split_in_half([])
([], [])
split_in_half([1])
([], [1])
~~~
#### Bonus
For a bonus, make sure your split_in_half function works for all sequences.

In addition to lists, strings, tuples and other sequences should also be accepted:
~~~
split_in_half("This is a string")
('This is ', 'a string')
split_in_half((1, 2, 3, 4, 5, 6))
((1, 2, 3), (4, 5, 6))
split_in_half(b"bytestring")
(b'bytes', b'tring')
~~~
Note that the returned items should be the same type as the original sequence.
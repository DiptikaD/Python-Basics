### Create a function characters that takes a string and returns a list where each item is a single character from the string.
~~~
characters("hello")
['h', 'e', 'l', 'l', 'o']
~~~
All characters should be lowercased:
~~~
characters("Trey Hunner")
['t', 'r', 'e', 'y', ' ', 'h', 'u', 'n', 'n', 'e', 'r']
~~~
### Bonus
As a bonus, your function should also accept an optional sort argument that, when True, will return the characters in ASCII-betical sorted order.
~~~
characters("Trey Hunner", sort=True)
[' ', 'e', 'e', 'h', 'n', 'n', 'r', 'r', 't', 'u', 'y']
characters("hello", sort=True)
['e', 'h', 'l', 'l', 'o']
~~~
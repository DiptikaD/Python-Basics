### For this exercise I want you to write a function that takes a dictionary of lists and returns a "flipped" dictionary of lists. What I mean by "flipped" is this:
~~~
d = {'a': [1, 2], 'b': [3, 1], 'c': [2]}
flip_dict_of_lists(d)
{1: ['a', 'b'], 2: ['a', 'c'], 3: ['b']}
~~~
Your function should accept any dictionary type and the output lists should maintain the order of given keys.

### Bonus 1
As a bonus, allow your function to accept a dict_type argument that will return a new dictionary-like object when called:
~~~
from collections import OrderedDict
toppings = OrderedDict({'Trey': ['anchovies', 'olives'], 'Guido': ['olives', 'pineapple']})
flip_dict_of_lists(toppings, dict_type=OrderedDict)
OrderedDict({'anchovies': ['Trey'], 'olives': ['Trey', 'Guido'], 'pineapple': ['Guido']})
~~~
### Bonus 2
As a second bonus, allow your function to accept a key_func argument that will be called to normalize the keys in the new dictionary:
~~~
toppings = {'Trey': ['anchovies', 'olives'], 'Guido': ['Olives', 'Pineapple']}
def lowercase(string): return string.lower()

flip_dict_of_lists(toppings, key_func=lowercase)
{'anchovies': ['Trey'], 'olives': ['Trey', 'Guido'], 'pineapple': ['Guido']}
~~~
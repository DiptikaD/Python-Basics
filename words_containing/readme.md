### Create a function called words_containing that locates all words containing a given letter.

This function should accept a list of words and a letter and should return a list of all given words that contain the given letter.
~~~
zen_line_2 = ["Explicit", "is", "better", "than", "implicit"]
words_containing(zen_line_2, "p")
['Explicit', 'implicit']
words_containing(zen_line_2, "i")
['Explicit', 'is', 'implicit']
words_containing(zen_line_2, "x")
['Explicit']
~~~
### Bonus
For a bonus, ensure your words_containing function ignores the capitalization of the given words:
~~~
zen_line_2 = ["Explicit", "is", "better", "than", "implicit"]
words_containing(zen_line_2, "e")
['Explicit', 'better']
words_containing(zen_line_2, "X")
['Explicit']
~~~
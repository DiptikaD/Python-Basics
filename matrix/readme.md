### I want you to write a function that accepts a string containing lines of numbers and returns a list of lists of numbers.

For example:
~~~
matrix_from_string("3 4 5")
[[3.0, 4.0, 5.0]]
matrix_from_string("3 4 5\n6 7 8")
[[3.0, 4.0, 5.0], [6.0, 7.0, 8.0]]
~~~
Make sure your function handles strings with an extra newline at the end:
~~~
matrix_from_string("1 2 3\n4 5 6\n7 8 9\n ")
[[1.0, 2.0, 3.0], [4.0, 5.0, 6.0], [7.0, 8.0, 9.0]]
~~~
### Bonus
As a bonus, make sure your function ignores extra whitespace:
~~~
matrix_from_string("""
    1   2   3

    4   5   6

    7   8   9
""")

[[1.0, 2.0, 3.0], [4.0, 5.0, 6.0], [7.0, 8.0, 9.0]]
~~~
Extra whitespace includes additional spaces before, after, or between numbers and extra blank lines between lines.
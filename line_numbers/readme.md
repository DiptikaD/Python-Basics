Write a program line_numbers.py that accepts a file as its only argument and prints out the lines in the files with a line number displayed in front of them. If my_file.txt contains the following text:

``This file``

``is two lines long.``

``No wait, it's three lines long!``

Then running this is what passing my_file.txt to line_numbers.py would look like:

```
$ python line_numbers.py my_file.txt
1 This file
2 is two lines long.
3 No wait, it's three lines long!```
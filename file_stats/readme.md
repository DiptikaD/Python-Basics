Write a program that accepts a file as an argument and outputs the number of lines and words in the file.

Given this file:

``This is a file.``

`With two lines in it.`

Running file_stats.py should look like this:

``$ python file_stats.py my_file.txt``

``Lines: 2``

``Words: 9``

For this exercise, you can assume that each "word" is separated by whitespace from each other word.

If the file ends in a newline character, that newline should not be counted (check the hints for a string method to help with this).
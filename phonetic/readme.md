### I'd like you to write a program which will help spell words phonetically using the NATO phonetic alphabet.

Your program should accept a string as a command-line argument and should print out a separate word for each letter in the given string:
~~~
$ python phonetic.py Python
Papa
Yankee
Tango
Hotel
Oscar
November
~~~
Unknown symbols (punctuation) should be ignored.

~~~
$ python phonetic.py "Yay!"
Yankee
Alfa
Yankee
~~~
And if no arguments are given, the user should be prompted for input:
~~~
$ python phonetic.py
Text to spell out: Trey
Tango
Romeo
Echo
Yankee
~~~
Note that Text to spell out: was printed by the program above and Trey was input by the user.

### Bonus 1
For the first bonus, make your program accepts multiple words, either via separate command-line arguments or an argument with spaces in it.

When printing out the spelling of multiple words, an empty line should appear between words.
~~~
$ python phonetic.py
Text to spell out: Python is lovely
Papa
Yankee
Tango
Hotel
Oscar
November

India
Sierra

Lima
Oscar
Victor
Echo
Lima
Yankee
~~~
### Bonus 2
For the second bonus, I'd like your program to accept an optional -f command-line option which can be used for passing a file of letters and words to use for spelling.

For example this file, words.txt:
~~~
a Apples
b Butter
c Charlie
d Duff
e Edward
f Freddy
g George
h Harry
i Ink
j Johnnie
k King
l London
m Monkey
n Nuts
o Orange
p Pudding
q Queenie
r Robert
s Sugar
t Tommy
u Uncle
v Vinegar
w Willie
x Xerxes
y Yellow
z Zebra
~~~
Calling our program using this file would look like this:
~~~
$ python phonetic.py -f words.txt PyCon
Pudding
Yellow
Charlie
Orange
Nuts
~~~
Note that this file shouldn't be limited to the 26 English letters: it should also be able to include digits or non-latin letters that can be spelled-out as well.

### Bonus 3
For the third bonus, I'd like you to ignore accents on accented characters.

For example:
~~~
$ python phonetic.py
Text to spell out: Hâlo
Hotel
Alfa
Lima
Oscar
~~~

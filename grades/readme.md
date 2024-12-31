### I'd like you to write a percent_to_grade function which will take a percentage and convert it to a grade by using a specific flavor of the A-F grading system used in the US.

The rules:

Below 60 is F
From 60 to below 70 is D
From 70 to below 80 is C
From 80 to below 90 is B
90 and above is A
~~~
percent_to_grade(72.5)
'C'
percent_to_grade(89.6)
'B'
percent_to_grade(60)
'D'
percent_to_grade(100)
'A'
percent_to_grade(2)
'F'
~~~

### Bonus 1
For the first bonus I'd like you to allow a keyword-only suffix argument to be passed to your percent_to_grade function. When suffix is True, you should add - and + suffixes to the grade according to another set of rules:

97 and above is A+
From 93 to below 97 is A
From 90 to below 93 is A-
From 87 to below 90 is B+
From 83 to below 87 is B
From 80 to below 83 is B-
From 77 to below 80 is C+
From 73 to below 77 is C
From 70 to below 73 is C-
From 67 to below 70 is D+
From 63 to below 67 is D
From 60 to below 63 is D-
Below 60 is F (no + or -)

~~~
percent_to_grade(72.5, suffix=True)
'C-'
percent_to_grade(89.6, suffix=True)
'B+'
percent_to_grade(60, suffix=True)
'D-'
percent_to_grade(100, suffix=True)
'A+'
percent_to_grade(2, suffix=True)
'F'
~~~

### Bonus 2
For the second bonus, I'd like you to accept another optional keyword-only argument: round. When round is True you should round percentages to their nearest whole number before calculating grades, with .5 always rounding upward.

~~~
percent_to_grade(69.4, round=True)
'D'
percent_to_grade(69.6, round=True)
'C'
percent_to_grade(72.5, suffix=True, round=True)
'C'
percent_to_grade(89.6, suffix=True, round=True)
'A-'
~~~

### Bonus 3
For the third bonus, I'd like you to create another function called calculate_gpa which accepts a sequence of letter grades and returns the grade point average based on the following rules:

A+ is worth 4.33
A is worth 4.00
A- is worth 3.67
B+ is worth 3.33
B is worth 3.00
B- is worth 2.67
C+ is worth 2.33
C is worth 2.00
C- is worth 1.67
D+ is worth 1.33
D is worth 1.00
D- is worth 0.67
F is worth 0.00
~~~
calculate_gpa(['D+', 'C', 'A-', 'B'])
2.5
calculate_gpa(['B+', 'A', 'C+', 'F'])
2.415
~~~
This exercise will count toward your final grade.
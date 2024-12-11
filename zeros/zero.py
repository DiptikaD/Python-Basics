# Problem Statement
# I'd like you to make a zero.py Python script which prints out 80 0 characters.

# Bonus 1
# For the first bonus, your zero.py program should accept an optional argument to customize the number of zeroes to print.

# Bonus 2
# For the second bonus, your zero.py program should accept any number of numeric arguments. Each argument should result in another line printed out.

import sys

request = sys.argv[1:] or [80]

for n in request:
    print("0" * int(n))

# this solution comes with help from roll.py
# simply the cli is read with sys.argv, if there is a number or a list of numbers present, then the for loop will multiply the "0" by those numbers, else the default is 80

# all tests pass
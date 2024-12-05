
#variables in python are not strongly typed. variables will update the value based on the most current assignment
amount = 3
amount = "three"

#can set a type hint for the user to know what the type should be, however python will ignore it. using type checkers like mypy will flag it as an error
amount : int = 3
amount = "three"

#integer division operator returns how many times one whole number fully divides into another
26//7
# output = 3. this is because 7 > 14 > 21 > 28
# it can divide up to 21 with remainder, but it took 3 times div to get to 26.

26%7
# output = 5. it is the remainder left over after dividing the full numbers.

#operator for exponential operations 
2**10
# output = 1024. this is 2^10
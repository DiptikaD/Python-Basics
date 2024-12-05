
#variables in python are not strongly typed. variables will update the value based on the most current assignment
amount = 3
amount = "three"

#can set a type hint for the user to know what the type should be, however python will ignore it. using type checkers like mypy will flag it as an error
amount : int = 3
amount = "three"
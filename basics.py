
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

##################################

#Strings
message = "moka is weird"
print(message.upper())
print(message.capitalize())
print(len(message))
print(message.islower())
print(message + "!")
print(message.replace("weird", "stinky"))
#keep quotes consistent "" '' and use escape characters if needed \n \' \t

# read tracebacks from bottom upward for most oldest at the bottom of the message, and newest at top.

# print() does not have a return value, it is None (py versions of void)

# to run py on cmd, navigate to the dir containing the file. then 
#python3 basics.py
#it will run all the code and print output

#can easily parse 
four = 4
fourStr = str(four)
print(fourStr)
fourInt = int(fourStr)
print(fourInt)

## input and output is easy
name = input("Who is this?? ")
print("oh its " + name + "!")

#could have also written as
print(f"oh its {name}!")
#this is a fstring, py looks for the code within {} and will convert the variable or code to fit into the fstring. it saves having to put +s and str(5) to convert ints into str.

#string join method - for converting a list of strings into one string with a joining common
colors = ["purple", "blue", "green", "orange"]
joined_colors = ", ".join(colors)
print(joined_colors)
#how does it know i do not want , at the start? dunno, but its a quick solution to having to iterate

#also works for ints too!
digits = range(10)
digit_string = "".join(str(n) for n in digits)
print(digit_string)

# REPL can be used on command prompt by typing "python3" for a responsive IDE. it does not save your work, but it acts as a playground to try snippets of code. 
# you can also have a pop-out window which might eliminate code visualisation errors using: python3 -m idlelib
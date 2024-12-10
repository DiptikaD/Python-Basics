# Problem Statement
# Create a program roll.py that simulates rolling a 6-sided die.

# BONUS1
# For the first bonus, accept a single argument representing the number of sides on the die to roll. If no argument is given, assume a single 6 sided die.

# BONUS2
# For the second bonus, accept any number of arguments, each of which represent sides of a die to roll. Simulate the roll of each die, sum the total roll number, and print out the result. If no arguments are given, assume a single 6 sided die.

import random
import sys

# #SOLUTION for program input
# roll = input()
# if roll == "":
#     print(random.randrange(6)+1)
# else: print(random.randrange(int(roll)))


# #SOLUTION for base problem
# #arguments from cli are included in code via the sys function- sys.argv[1] (for the first argument). This is if the user calls upon the program in cli: roll.py 20 
# if len(sys.argv) > 1:
#     faces = int(sys.argv[1])
# else:
#     faces = 6

# print(random.randint(1,faces))

#SOLUTION for bonus 1 + 2
# sys.argv[1:] is a truthy statement, if there is an argument, then it will use the first index, else it is false and will do the default value [6]. in the for loop, depending on the length of the list form sys.argv, it will roll and add to the total.
face_counts = sys.argv[1:] or [6]
roll =0
for n in face_counts:
    roll += random.randint(1,int(n))
print(roll)

#navigating to file and typing python roll.py 20 10
#will have the module roll 20, add to sum, then roll 10 and add to sum. print sum.

#running test_roll.py gives successes and unexpected successed for the bonus points.
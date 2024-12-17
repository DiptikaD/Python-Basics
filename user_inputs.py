    # strings can be multi lined using the """ function
yell = "yell"
how_to_handle_moka = f"""she will hunt down your food and hide it
she will also {yell} at anyone that walks past outside
she goes wild over any noise outside the house"""

print(how_to_handle_moka)

    # can prompt in input and sad it to a variable to be used later
emotion = input("How do you feel about moka? \n")

    # turns out we could oneline this whole thing, but it would be hard to read
# name = input("enter a name\n")
adjective = input("enter an adjective: ")
noun = input("enter an noun: ")

print(f""" {input("enter a name: ")} is a very {adjective} {noun} """)

    ## command line arguments vs function arguments
    ## commandline args are passed through the commandline when invoking the program "python3 user_inputs moka". must import sys, then invoke with sys.argv[1], as [0] = user_inputs, [1] = moka. NOTE all cmd args are STRINGS and must be converted as needed.
    ## function arguments are parameters passed through a function "range(1,11)"

import sys

if len(sys.argv)>1:
    name = sys.argv[1]
    print(f"Hello {name}!")
    
else: print("Hello World!")

    ## here is a turnery alternate to the above. [1:] writes in all arguments at [1]+, then arguments[0] is the first arg after the program name (because of how the variables are set)

arguments = sys.argv[1:]

name = arguments[0] if arguments else "world"
print(f"Hello {name}!")

    ## sys.argv vs argparser
    ## argparser is a user-friendly version of sys.argv, it has alot more code, but it provides quality of life commands for users
    ## --verbose; to spell out what is going on
    ## --help; to provide information of the input required
    ## helpful error messages
[program, x, y] = sys.argv
print(float(x) + float(y))

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('x', type=float)
parser.add_argument('y', type=float)
args = parser.parse_args()
print(args.x+args.y)


    ## number formatting
# num = 4
# print("{num:.2f}", f"{num:.2f}", "2 digits after decimal", sep="\t")
# print("{num:02}", f"{num:02}", "0-pad to 2 digits", sep="\t")
# print("{num: 3}", f"{num: 3}", "space-pad to 3 digits", sep="\t")
# print("{num:.0%}", f"{num:.0%}", "format as percent with 0 digits after decimal", sep="\t")
# print("{num**6:,}", f"{num**6:,}", "add commas as thousands separators", sep="\t")